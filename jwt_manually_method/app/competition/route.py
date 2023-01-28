from fastapi import APIRouter, Depends, HTTPException, status
from app.competition.schemas import CreateCompetition, ResponseCompetition
from sqlalchemy.orm import Session
from app.competition.models import CompetitionTable
from app.database import get_db
from app.utils.jwt_bearer import get_current_user
from app.user.model  import User

competition = APIRouter()

@competition.post('/competition', response_model = ResponseCompetition)
async def create_competition(request: CreateCompetition ,  db : Session = Depends(get_db), user: str = Depends(get_current_user)):

    db_user = db.query(User).filter(User.id == user).first()    
    
    new_competition = CompetitionTable(name= request.name, status= request.status, description= request.description, created_by = db_user.id)
    
    db.add(new_competition)
    db.commit()
    db.refresh(new_competition)

    return new_competition

@competition.get('/competition/all', response_model = list[ResponseCompetition])
async def all_competitions(db : Session = Depends(get_db), user: str = Depends(get_current_user)):

    info_all_competition = db.query(CompetitionTable).all()
    return info_all_competition
 
@competition.get('/competition/{id}', response_model = ResponseCompetition)
async def particular_competition(id, db : Session = Depends(get_db), user: User = Depends(get_current_user)):

    try:
        info_particular_competition = db.query(CompetitionTable).filter(CompetitionTable.id == id).first()
        return info_particular_competition
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="ID Not Found 😶‍🌫️")

@competition.put('/update_competition/{id}')
async def update_competition (id, request:CreateCompetition, db : Session = Depends(get_db), user: User = Depends(get_current_user)):
    
    try:
        db.query(CompetitionTable).filter(CompetitionTable.id == id).update(request.dict())
        db.commit()
        return { "massage":"Successfully Update"}
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="ID Not Found 😶‍🌫️")

@competition.delete('/delete_competition/{id}')
async def delete_competition(id, db : Session = Depends(get_db), user: str = Depends(get_current_user)):

    try:
        db.query(CompetitionTable).filter(CompetitionTable.id == id).delete()
        db.commit()
        return {"message":"Delete successfully"}
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="ID Not Found 😶‍🌫️")