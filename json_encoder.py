from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from datetime import datetime

app = FastAPI()

# Using the jsonable_encoder

fake_db = {}

class Item(BaseModel):
    title :str
    timestamp : datetime
    descripton : str | None = None

@app.put("items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data