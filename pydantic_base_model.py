from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Pakage(BaseModel):
    name : str
    number : int
    description : Optional[str]  = None

app = FastAPI()

@app.post("/pakage/{priority}")
def make_pakage(priority : int, pakage : Pakage, value: bool):
    return {"priority " : priority, **pakage.dict(), "value " : value}