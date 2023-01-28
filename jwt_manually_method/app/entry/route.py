from fastapi import APIRouter, Depends, HTTPException, status
from app.entry.schemas import CreateEntry, ResponseEntry
from sqlalchemy.orm import Session
from app.entry.models import EntryTable
from app.database import get_db
from app.entry.models import EntryTable
from app.utils.jwt_bearer import  get_current_user
from app.user.model import User 
from app.competition.models import CompetitionTable

entry = APIRouter()

@entry.post('/entry', response_model= ResponseEntry)
async def get_entry(request : CreateEntry, db : Session = Depends(get_db), user: str = Depends(get_current_user)):

    db_user= db.query(User).filter(User.id == user).first()
    
    db_competition = db.query(CompetitionTable).filter(CompetitionTable.created_by == db_user.id).first()
    new_entry = EntryTable(title = request.title,
                           topic = request.topic, 
                           state = request.state,
                           country = request.country, 
                           created_by = db_competition.id)

    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

@entry.get('/entry/all', response_model= list[ResponseEntry])
async def get_all_entry(db : Session= Depends(get_db), user: str = Depends(get_current_user)):

    all_entry = db.query(EntryTable).all()
    return all_entry   

@entry.get('/entry/{id}', response_model= ResponseEntry)
async def get_particular_entry(id, db : Session= Depends(get_db), user: str = Depends(get_current_user)):

    try:
        particular_entry = db.query(EntryTable).filter(EntryTable.id == id).first()
        return particular_entry
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="ID Not Found 😶‍🌫️")

@entry.put('/update_entry/{id}')
async def update_entry( request:CreateEntry, id, db : Session = Depends(get_db), user: str = Depends(get_current_user)):

    try:
        db.query(EntryTable).filter(EntryTable.id == id).update(request.dict())
        db.commit()
        return { "massage":"Successfully Update 😁"}
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="ID Not Found 😶‍🌫️")

@entry.delete('/delete_entry/{id}')
async def delete_entry(id, db : Session = Depends(get_db), user: str = Depends(get_current_user)):
    
    try:
        db.query(EntryTable).filter(EntryTable.id == id).delete()
        db.commit()
        return {"message":"Delete successfully 👍"}
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="ID Not Found 😶‍🌫️")