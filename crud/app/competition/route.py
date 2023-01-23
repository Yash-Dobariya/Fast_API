from fastapi import APIRouter, Depends
from app.competition.schemas import CreateCompetition, ResponseCompetition
from sqlalchemy.orm import Session
from app.competition.models import CompetitionTable
from app.database.database import get_db


competition = APIRouter()

@competition.post('/competition', response_model =ResponseCompetition)
async def create_competition( request: CreateCompetition, db : Session = Depends(get_db)):
    new_competition = CompetitionTable(user_id = request.user_id,name= request.name, 
                                       status= request.status, description= request.description)
    db.add(new_competition)
    db.commit()
    db.refresh(new_competition)
    return new_competition

@competition.get('/competition/all', response_model = list[ResponseCompetition] )
async def all_competitions(db : Session = Depends(get_db)):
    info_all_competition = db.query(CompetitionTable).all()
    return info_all_competition

@competition.get('/competition/{id}', response_model = ResponseCompetition)
async def particular_competition(id, db : Session = Depends(get_db)):
    info_particular_competition = db.query(CompetitionTable.id == id).first()
    return info_particular_competition

@competition.put('/update_competition/{id}')
async def update_competition(id, request:CreateCompetition, db : Session = Depends(get_db)):
    update_detail = db.query(CompetitionTable).filter(CompetitionTable.id == id).update(request.dict())
    db.commit()
    return { "massage":"Successfully Update"}

@competition.delete('/delete_competition/{id}')
async def delete_competition(id, db : Session = Depends(get_db)):
    db.query(CompetitionTable).filter(CompetitionTable.id == id).delete()
    db.commit()
    return {"message":"Delete successfully"}