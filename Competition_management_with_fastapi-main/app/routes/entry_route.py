from fastapi import APIRouter , Depends
from app.database.database import get_db , engine ,SessionLocal
from app.schemas.entry_schema import *
from app.models.entry_model import Entry_Table
from app.models.competition_model import Competition
from sqlalchemy.orm import Session
from typing import List

entry = APIRouter()

#This api get all entry details
@entry.get("/entry",tags=['entry'],response_model=List[CreateEntry])
def allentry(db:Session = Depends(get_db)):
    db_entry = db.query(Entry_Table).all()

    return db_entry


#This create new entry
@entry.post("/entryadd",tags=['entry'],response_model= CreateEntry)
def addentry(request:CreateEntry , db:Session = Depends(get_db)):

    new_entry = Entry_Table(id = request.id , title = request.title , topic = request.topic , state = request.state , 
                            country = request.country , competition_id = request.competition_id )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return new_entry


#Update entry by id
@entry.put("/updateentry/{id}",tags=['entry'])
def updateentry(id,request:CreateEntry , db:Session = Depends(get_db)):
    db.query(Entry_Table).filter(Entry_Table.id == id).update(request.dict())
    db.commit()

    return "done"


#Delete entry by id
@entry.delete("/entrydelete/{id}",tags=['entry'])
def deleteentry(id, db:Session = Depends(get_db)):
    db.query(Entry_Table).filter(Entry_Table.id == id).delete(synchronize_session=False)
    db.commit()

    return "done"


#User entry count
@entry.get('/entrycount/{user_id}')
def count_user(user_id, db: Session = Depends(get_db)):

    competitions = db.query(Competition.id).filter(Competition.user_id == user_id).all()
    competitions = [competition.id for competition in competitions]
    result = 0

    for competition in competitions:
        entry = (db.query(Entry_Table.id).filter(Entry_Table.competition_id == competition).count())
        result += entry

    return result
