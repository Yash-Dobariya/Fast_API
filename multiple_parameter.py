# Mix Path, Query and body parameters

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name : str
    description : str
    price : int
    tax : float

# Mix Path, Query and body parameters

@app.put("/items/{item_id}/body_parameter")
def update_item(*, item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),q : str | None = None, item :Item  ):
    results = {"item_id": item_id, "q": q, "item":item}
    return results

# Multiple body parameters

class User(BaseModel):
    username: str
    full_name: str | None =  None

@app.put("/items/{items_id}/multiple_body_parameter")
def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results

# Singular values in body

@app.put("/items/{item_id}/singular_valiue")
def update_item(item_id: int, item: Item, user: User, importance: int = Body()):
    results = {"item_id": item_id, "item": item, "user":user, "importance":importance}
    return results

# Multiple body params and query

@app.put("/items/{items_id}/multiple_body_parameter_query")
def update_item(*,item_id: int,
                item: Item,
                user: User,
                importance: int = Body(gt=0),
                q: str | None = None):

    results = {"item_id": item_id, "item": item, "user":user, "importance":importance,"q":q}
    return results