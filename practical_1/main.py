from fastapi import FastAPI, status
from pydantic import BaseModel
from database import SessionLocal
import models
from typing import List

app = FastAPI()

class Item(BaseModel):
    id : int
    name : str 
    description : str 
    price : int
    on_offer : bool

    class Config:
        orm_mode = True


db=SessionLocal()

@app.get('/items', response_model=List[Item], status_code=status.HTTP_200_OK)
def get_all_items():
    items = db.query(models.Item).all()
    return items

@app.get('/items/{item_id}')
def get_an_item(item_id: int):
    pass

@app.post('/items', response_model=Item, status_code=status.HTTP_201_CREATED)
def create_an_item(item: Item):
    new_item = models.Item()
    db.add(new_item)
    db.commit()
    return new_item

@app.put('/item')
def update_an_item(item_id: int):
    pass

@app.delete('/item')
def delete_item(item_id: int):
    pass