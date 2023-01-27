from fastapi import APIRouter, Depends, HTTPException, status
from app.entry.schemas import CreateEntry, ResponseEntry
from sqlalchemy.orm import Session
from app.entry.models import EntryTable
from app.database import get_db
from fastapi_jwt_auth import AuthJWT
from app.utils.token import get_config
from app.entry.models import EntryTable
from app.competition.models import CompetitionTable


entry = APIRouter()

@entry.post('/entry', response_model=ResponseEntry)
async def get_entry(Authorize : AuthJWT = Depends(get_config), *, request : CreateEntry, db : Session = Depends(get_db)):
    try:
        Authorize.jwt_required()
        current_user =  Authorize.get_jwt_subject()
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid access Token 😢")

    competition_user = db.query(CompetitionTable).filter(CompetitionTable.created_by == current_user).first()
    new_entry = EntryTable(title = request.title, topic = request.topic, state = request.state, country = request.country, created_by = competition_user.id)
    
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return new_entry
    
@entry.get('/entry/all', response_model= list[ResponseEntry])
async def get_all_entry( Authorize : AuthJWT = Depends(get_config), db : Session= Depends(get_db)):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid access Token 😢")

    all_entry = db.query(EntryTable).all()
    return all_entry

@entry.get('/entry/{id}', response_model= ResponseEntry)
async def get_particular_entry(Authorize : AuthJWT = Depends(get_config), *, id, db : Session= Depends(get_db)):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid access Token 😢")

    particular_entry = db.query(EntryTable).filter(EntryTable.id == id).first()
    return particular_entry

@entry.put('/update_entry/{id}')
async def update_entry(request:CreateEntry, Authorize : AuthJWT = Depends(get_config), *,id,db : Session = Depends(get_db)):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid access Token 😢")

    db.query(EntryTable).filter(EntryTable.id == id).update(request.dict())
    db.commit()
    return { "massage":"Successfully Update"}

@entry.delete('/delete_entry/{id}')
async def delete_entry( Authorize : AuthJWT = Depends(get_config), *,id, db : Session = Depends(get_db)):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid access Token 😢")

    db.query(EntryTable).filter(EntryTable.id == id).delete()
    db.commit()
    return {"message":"Delete successfully"}
