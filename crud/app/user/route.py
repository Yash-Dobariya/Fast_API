from fastapi import APIRouter, Depends
from app.user.schemas import CreateUser, ResponseUser
from sqlalchemy.orm import Session
from app.user.models import UserTable
from app.database.database import get_db

user = APIRouter()

@user.post('/detail',tags=["User"], response_model = ResponseUser)
async def create_user(request: CreateUser, db:Session= Depends(get_db) ):
    new_user = UserTable(name= request.name, birth_date= request.birth_date, gender= request.gender )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@user.get('/detail/all',tags=["User"],response_model = list[ResponseUser])
async def get_all_user(db: Session = Depends(get_db) ):
    all_user = db.query(UserTable).all()
    return all_user

@user.get('/detail/{id}',tags=["User"], response_model = ResponseUser)
async def get_particular_user(id, db: Session = Depends(get_db) ):
    particular_user = db.query(UserTable).filter(UserTable.id == id).first()
    return particular_user

@user.put('/update_detail/{id}',tags=["User"])
async def update_user(id, request:CreateUser, db: Session = Depends(get_db)):
    detail = db.query(UserTable).filter(UserTable.id == id).update(request.dict())
    db.commit()
    return { "massage":"Successfully Update"}

@user.delete('/delete_detail/{id}',tags=["User"])
async def delete_user(id, db: Session = Depends(get_db)):
    remove_user = db.query(UserTable).filter(UserTable.id == id).delete()
    db.commit()
    return {"message":"Delete successfully"}