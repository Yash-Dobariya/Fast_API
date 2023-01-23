from pydantic import BaseModel


class CreateCompetition(BaseModel):

    name : str
    status : str
    description : str
    user_id : int    

    
class ResponseCompetition(BaseModel):

    id : int
    name : str
    status : str
    description : str
    user_id : int 
    

    class Config:
        orm_mode = True

