from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class CreateUser(BaseModel):

    name : str 
    birth_date: Optional[date] = date(year=2023 ,month= 2 ,day= 17)
    gender : Optional[str]=None

class ResponseUser(BaseModel):

    id : int
    name : str | None
    birth_date : date
    gender : str
    
    class Config:
        orm_mode = True