from pydantic import BaseModel
import uuid


class CreateCompetition(BaseModel):

    name : str
    status : str
    description : str
    
    
class ResponseCompetition(BaseModel):

    id : uuid.UUID
    name : str
    status : str
    description : str

    

    class Config:
        orm_mode = True

