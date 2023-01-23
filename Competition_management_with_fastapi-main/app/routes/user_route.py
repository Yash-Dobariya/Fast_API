from fastapi import APIRouter , Depends
from app.database.database import get_db , engine ,SessionLocal
from app.schemas.user_schema import *
from app.models.user_model import User
from sqlalchemy.orm import Session
from typing import List

userdata = APIRouter()

#Get all user details
@userdata.get("/user",tags=['users'],response_model=List[DisplayUsers])
def alluser(db:Session = Depends(get_db)):
    db_users = db.query(User).all()

    return db_users


#Get user details by name
@userdata.get("/users/{name}",tags=['users'],response_model=DisplayUsers)
def showusersbyname(name,db:Session = Depends(get_db)):
    db_users = db.query(User).filter(User.name == name).first()

    return db_users


#Create new user
@userdata.post("/useradd",tags=['users'], response_model=DisplayUsers)
def addusers(request:CreateUsers , db:Session = Depends(get_db)):

    new_users = User(name = request.name, birth_date = request.birth_date, gender = request.gender)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)

    return new_users


#Update user details by name
@userdata.put("/updateusers/{name}",tags=['users'])
def updateusers(name,request:CreateUsers , db:Session = Depends(get_db)):
    db.query(User).filter(User.name == name).update(request.dict())
    db.commit()

    return "done"


#Delete user details by name
@userdata.delete("/usersdelete/{name}",tags=['users'])
def users4(name, db:Session = Depends(get_db)):
    db.query(User).filter(User.name == name).delete(synchronize_session=False)
    db.commit()

    return "done"
