from fastapi import APIRouter, Depends, HTTPException, status
from app.competition.schemas import CreateCompetition, ResponseCompetition
from sqlalchemy.orm import Session
from app.competition.models import CompetitionTable
from app.database import get_db
from fastapi_jwt_auth import AuthJWT
from app.utils.token import get_config
# from app.competition.models import CompetitionTable



competition = APIRouter()

@competition.post('/competition', response_model =ResponseCompetition)
async def create_competition(Authorize : AuthJWT = Depends(get_config), *, request: CreateCompetition ,  db : Session = Depends(get_db)):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid access Token 😢")

    new_competition = CompetitionTable(name= request.name, status= request.status, description= request.description)
    
    db.add(new_competition)
    db.commit()
    db.refresh(new_competition)
    return new_competition

@competition.get('/competition/all', response_model = list[ResponseCompetition] )
async def all_competitions(Authorize : AuthJWT = Depends(get_config), db : Session = Depends(get_db)):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid access Token 😢")

    info_all_competition = db.query(CompetitionTable).all()
    return info_all_competition

@competition.get('/competition/{id}', response_model = ResponseCompetition)
async def particular_competition( Authorize : AuthJWT = Depends(get_config), *,id, db : Session = Depends(get_db)):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid access Token 😢")

    info_particular_competition = db.query(CompetitionTable).filter(CompetitionTable.id == id).first()
    return info_particular_competition

@competition.put('/update_competition/{id}')
async def update_competition(Authorize : AuthJWT = Depends(get_config), *, id, request:CreateCompetition, db : Session = Depends(get_db)):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid access Token 😢")

    db.query(CompetitionTable).filter(CompetitionTable.id == id).update(request.dict())
    db.commit()
    return { "massage":"Successfully Update"}

@competition.delete('/delete_competition/{id}')
async def delete_competition( Authorize : AuthJWT = Depends(get_config), *, id, db : Session = Depends(get_db)):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid access Token 😢")

    db.query(CompetitionTable).filter(CompetitionTable.id == id).delete()
    db.commit()
    return {"message":"Delete successfully"}