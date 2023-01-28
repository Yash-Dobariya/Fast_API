from fastapi import APIRouter, Depends, HTTPException, status
from app.competition.schemas import CreateCompetition, ResponseCompetition
from sqlalchemy.orm import Session
from app.competition.models import CompetitionTable
from app.database import get_db
from fastapi_jwt_auth import AuthJWT
from app.utils.token import get_current_user


competition = APIRouter()

@competition.post('/competition', response_model = ResponseCompetition)
async def create_competition( request: CreateCompetition, user : str = Depends(get_current_user), db : Session = Depends(get_db)):

    new_competition = CompetitionTable(name= request.name, status= request.status, description= request.description, created_by = user)
    
    db.add(new_competition)
    db.commit()
    db.refresh(new_competition)

    return new_competition

@competition.get('/competition/all', response_model = list[ResponseCompetition] )
async def all_competitions(user : str = Depends(get_current_user), db : Session = Depends(get_db)):

    info_all_competition = db.query(CompetitionTable).all()
    
    return info_all_competition

@competition.get('/competition/{id}', response_model = ResponseCompetition)
async def particular_competition(id, user : str = Depends(get_current_user), db : Session = Depends(get_db)):

    try:
        info_particular_competition = db.query(CompetitionTable).filter(CompetitionTable.id == id).first()
        return info_particular_competition
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="ID Not Found 😶‍🌫️")

@competition.put('/update_competition/{id}')
async def update_competition(id, request:CreateCompetition, user : str = Depends(get_current_user), db : Session = Depends(get_db)):

    try:
        db.query(CompetitionTable).filter(CompetitionTable.id == id).update(request.dict())
        db.commit()
        return { "massage":"Successfully Update 😁"}
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="ID Not Found 😶‍🌫️")

@competition.delete('/delete_competition/{id}')
async def delete_competition(id, user : str = Depends(get_current_user), db : Session = Depends(get_db)):

    try:
        db.query(CompetitionTable).filter(CompetitionTable.id == id).delete()
        db.commit()
        return {"message":"Delete successfully 👍"}
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="ID Not Found 😶‍🌫️")