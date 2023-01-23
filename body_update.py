from fastapi import FastAPI
from pydantic import BaseModel
from json_encoder import jsonable_encoder

app = FastAPI()

class Item1(BaseModel):
    name : str | None = None
    description : str | None = None
    price : float | None = None
    tax :float = 10.5
    tags : list[str] = []

items ={"foo":{"name":"foo", "price":50.2},
        "bar":{"name":"baz","description": "The bartenders", "price": 62, "tax": 20.2},
        "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},}

@app.get("/item/{itemid}", response_model=Item1)
def read_item(item_id: str):
    return items[item_id]

@app.put("/itemss/{item_id}", response_model=Item1)
async def update_item(item_id: str, item: Item1 ):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded