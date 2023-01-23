from pydantic import BaseModel
from datetime import date
from typing import Optional
from app.utils.schemas import Commonschemas


#Demo schema for developer to unserstand the structure of competition table
class Competitions(BaseModel,Commonschemas):
    id: int
    name: str
    status: str
    description: str
    user_id: int


#Schema to take input and show the response
class CreateCompetition(BaseModel):
    id:int
    name:str
    status:str
    user_id:int
    description:str

    class Config:
        orm_mode = True
