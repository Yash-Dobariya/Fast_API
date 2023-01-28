from fastapi import APIRouter, Depends, HTTPException, status
from app.entry.schemas import CreateEntry, ResponseEntry
from sqlalchemy.orm import Session
from app.entry.models import EntryTable
from app.database import get_db
from app.utils.token import get_current_user
from app.entry.models import EntryTable
from app.competition.models import CompetitionTable


entry = APIRouter()

@entry.post('/entry', response_model=ResponseEntry)
async def get_entry(request : CreateEntry, user : str = Depends(get_current_user), db : Session = Depends(get_db)):

    competition_user = db.query(CompetitionTable).filter(CompetitionTable.created_by == user).first()
    new_entry = EntryTable(title = request.title, topic = request.topic, state = request.state, country = request.country, created_by = competition_user.id)
    
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return new_entry
    
@entry.get('/entry/all', response_model= list[ResponseEntry])
async def get_all_entry(user : str = Depends(get_current_user), db : Session= Depends(get_db)):

    all_entry = db.query(EntryTable).all()
    
    return all_entry

@entry.get('/entry/{id}', response_model= ResponseEntry)
async def get_particular_entry(id, user : str = Depends(get_current_user), db : Session= Depends(get_db)):
    
    try:
        particular_entry = db.query(EntryTable).filter(EntryTable.id == id).first()
        return particular_entry
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="ID Not Found 😶‍🌫️")
        
@entry.put('/update_entry/{id}')
async def update_entry(id, request:CreateEntry, user : str = Depends(get_current_user), db : Session = Depends(get_db)):

    try:
        db.query(EntryTable).filter(EntryTable.id == id).update(request.dict())
        db.commit()
        return { "massage":"Successfully Update 😁"}
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="ID Not Found 😶‍🌫️")

@entry.delete('/delete_entry/{id}')
async def delete_entry(id, user : str = Depends(get_current_user), db : Session = Depends(get_db)):

    try:
        db.query(EntryTable).filter(EntryTable.id == id).delete()
        db.commit()
        return {"message":"Delete successfully 👍"}
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="ID Not Found 😶‍🌫️")