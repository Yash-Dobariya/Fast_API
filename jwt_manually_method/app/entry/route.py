from fastapi import APIRouter, Depends, HTTPException, status, Request
from app.entry.schemas import CreateEntry, ResponseEntry
from sqlalchemy.orm import Session
from app.entry.models import EntryTable
from app.database import get_db
from app.utils.token import decode_access_token
from app.entry.models import EntryTable
from app.competition.models import CompetitionTable
from app.utils.jwt_bearer import get_current_user
from app.user.model import User 


entry = APIRouter()

@entry.post('/entry', response_model= ResponseEntry)
async def get_entry(current_user: User = Depends(get_current_user), *,request: Request,db_request : CreateEntry, db : Session = Depends(get_db)):

    try:
        access_token = request.headers["Authorization"][7:]
        user_id = current_user.id
        user = db.query(CompetitionTable).filter(CompetitionTable.created_by == user_id).first()

    except:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="invalid token")

    
    new_entry = EntryTable(title = db_request.title, topic = db_request.topic, state = db_request.state, country = db_request.country, created_by = user.id)

    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

@entry.get('/entry/all', response_model= list[ResponseEntry])
async def get_all_entry(current_user: User = Depends(get_current_user), db : Session= Depends(get_db)):
    try:
        all_entry = db.query(EntryTable).all()
        return all_entry

    except:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="invalid token")   

@entry.get('/entry/{id}', response_model= ResponseEntry)
async def get_particular_entry(current_user: User = Depends(get_current_user), *,id, db : Session= Depends(get_db)):
    try:
        particular_entry = db.query(EntryTable).filter(EntryTable.id == id).first()
        return particular_entry
    except:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="invalid token")

@entry.put('/update_entry/{id}')
async def update_entry(current_user: User = Depends(get_current_user), *, db_request:CreateEntry,id,db : Session = Depends(get_db)):
    try:
        db.query(EntryTable).filter(EntryTable.id == id).update(db_request.dict())
        db.commit()
        return { "massage":"Successfully Update"}
    except:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="invalid token")

@entry.delete('/delete_entry/{id}')
async def delete_entry(current_user: User = Depends(get_current_user), *, id, db : Session = Depends(get_db)):
    try:
        db.query(EntryTable).filter(EntryTable.id == id).delete()
        db.commit()
        return {"message":"Delete successfully"}
    except:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="invalid token")