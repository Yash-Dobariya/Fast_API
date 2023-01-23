from fastapi import APIRouter, Depends
from app.entry.schemas import CreateEntry, ResponseEntry
from sqlalchemy.orm import Session 
from app.entry.models import EntryTable
from app.database.database import get_db


entry = APIRouter()

@entry.post('/entry', response_model=ResponseEntry)
async def get_entry(request : CreateEntry, db : Session = Depends(get_db)):
    new_entry = EntryTable(title = request.title, topic = request.topic, state = request.state, 
                           country = request.country,competition_id= request.competition_id)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

@entry.get('/entry/all', response_model= list[ResponseEntry])
async def get_all_entry(db : Session= Depends(get_db)):
    all_entry = db.query(EntryTable).all()
    return all_entry

@entry.get('/entry/{id}', response_model= ResponseEntry)
async def get_particular_entry(id, db : Session= Depends(get_db)):
    particular_entry = db.query(EntryTable).filter(EntryTable.id == id).first()
    return particular_entry

@entry.put('/update_entry/{id}')
async def update_entry(id , request:CreateEntry , db : Session = Depends(get_db)):
    db.query(EntryTable).filter(EntryTable.id == id).update(request.dict())
    db.commit()
    return { "massage":"Successfully Update"}

@entry.delete('/delete_entry/{id}')
async def delete_entry(id, db : Session = Depends(get_db)):
    db.query(EntryTable).filter(EntryTable.id == id).delete()
    db.commit()
    return {"message":"Delete successfully"}
