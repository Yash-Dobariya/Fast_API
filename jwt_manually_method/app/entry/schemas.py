from pydantic import BaseModel
import uuid

class CreateEntry(BaseModel):

    title : str
    topic : str
    state : str
    country : str

class ResponseEntry(BaseModel):

    id : uuid.UUID
    title : str
    topic : str
    state : str
    country: str

    class Config:
        orm_mode = True