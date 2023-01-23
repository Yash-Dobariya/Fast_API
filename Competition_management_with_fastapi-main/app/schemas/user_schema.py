from pydantic import BaseModel , Field
from typing import Optional
from datetime import date
from app.utils.schemas import Commonschemas


#Demo schema for developer to unserstand the structure of user table
class Users(BaseModel,Commonschemas):
    id: int
    name: str
    birth_date: date
    gender: str


#Schema to take input
class CreateUsers(BaseModel):
    name:Optional[str]=None
    birth_date:Optional[date] = Field(default_factory=date(2022 , 12 , 12))
    gender:Optional[str]


#Schema for response
class DisplayUsers(BaseModel):
    id:int
    name:str
    birth_date:date
    gender:str

    class Config:
        orm_mode = True
