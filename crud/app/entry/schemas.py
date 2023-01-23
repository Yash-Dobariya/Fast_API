from pydantic import BaseModel


class CreateEntry(BaseModel):

    title : str
    topic : str
    state : str
    country : str
    competition_id : int

    class Config:
        orm_mode = True
    
class ResponseEntry(BaseModel):

    id : int
    title : str
    topic : str
    state : str
    country: str
    competition_id : int

    class Config:
        orm_mode = True