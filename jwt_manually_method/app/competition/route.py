from fastapi import APIRouter, Depends, HTTPException, status, Request
from app.competition.schemas import CreateCompetition, ResponseCompetition
from sqlalchemy.orm import Session
from app.competition.models import CompetitionTable
from app.database import get_db
from app.utils.jwt_bearer import get_current_user
from app.utils.token import decode_access_token
from app.user.model  import User

competition = APIRouter()

@competition.post('/competition', response_model = ResponseCompetition)
async def create_competition(current_user: User = Depends(get_current_user), *, request: Request, db_request: CreateCompetition ,  db : Session = Depends(get_db)):
    
    try:
        # access_token = request.headers["Authorization"][7:]
        user_id = current_user.id
        user = db.query(CompetitionTable).filter(CompetitionTable.created_by == user_id).first()    
        
    except: 
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="invalid Token")
    
    new_competition = CompetitionTable(name= db_request.name, status= db_request.status, description= db_request.description, created_by = user.id)
    
    db.add(new_competition)
    db.commit()
    db.refresh(new_competition)

    return new_competition

@competition.get('/competition/all' , response_model = list[ResponseCompetition] )
async def all_competitions(current_user: User = Depends(get_current_user), db : Session = Depends(get_db)):
    try:
        info_all_competition = db.query(CompetitionTable).all()
        return info_all_competition
    except:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="invalid Token")

@competition.get('/competition/{id}', response_model = ResponseCompetition)
async def particular_competition(current_user: User = Depends(get_current_user), *, id, db : Session = Depends(get_db)):
    try:
        info_particular_competition = db.query(CompetitionTable).filter(CompetitionTable.id == id).first()
        return info_particular_competition
    except:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="invalid Token")
        
@competition.put('/update_competition/{id}')
async def update_competition (current_user: User = Depends(get_current_user), *, id, db_request:CreateCompetition, db : Session = Depends(get_db)):
    try:
        db.query(CompetitionTable).filter(CompetitionTable.id == id).update(db_request.dict())
        db.commit()
        return { "massage":"Successfully Update"}
    except:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="invalid Token")

@competition.delete('/delete_competition/{id}')
async def delete_competition(current_user: User = Depends(get_current_user), *, id, db : Session = Depends(get_db)):
    try:
        db.query(CompetitionTable).filter(CompetitionTable.id == id).delete()
        db.commit()
        return {"message":"Delete successfully"}
    except:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="invalid Token")