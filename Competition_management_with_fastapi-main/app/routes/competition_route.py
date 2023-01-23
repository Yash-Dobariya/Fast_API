from fastapi import APIRouter , Depends
from app.database.database import get_db , engine ,SessionLocal
from app.schemas.competition_schema import *
from app.models.competition_model import Competition
from sqlalchemy.orm import Session
from typing import List

competition = APIRouter()

#Get all competition details
@competition.get("/competitonall",tags=['competition'],response_model=List[CreateCompetition])
def alluser(db:Session = Depends(get_db)):
    db_ucompetition = db.query(Competition).all()

    return db_ucompetition


#Get competition details by name
@competition.get("/competitionbyname/{name}",tags=['competition'],response_model=CreateCompetition)
def showusersbyname(name,db:Session = Depends(get_db)):
    db_competition = db.query(Competition).filter(Competition.name == name).first()

    return db_competition


#Create new competition
@competition.post("/competitionadd",tags=['competition'],response_model= CreateCompetition)
def addcompetition(request:CreateCompetition , db:Session = Depends(get_db)):

    new_competition = Competition(name = request.name ,description = request.description ,user_id = request.user_id, status = request.status  )
    db.add(new_competition)
    db.commit()
    db.refresh(new_competition)



    return new_competition


#Update competition by id
@competition.put("/updatecompetition/{id}",tags=['competition'])
def updateusers(id,request:CreateCompetition , db:Session = Depends(get_db)):

    db.query(Competition).filter(Competition.id == id).update(request.dict())
    db.commit()

    return "UPDATE done"


#Delete competition by id
@competition.delete("/competitiondelete/{id}",tags=['competition'])
def users4(id, db:Session = Depends(get_db)):

    db.query(Competition).filter(Competition.id == id).delete(synchronize_session=False)
    db.commit()

    return "DELETE done"
