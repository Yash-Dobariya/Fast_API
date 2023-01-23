from fastapi import FastAPI, status
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

# Response Status Code

class Item1(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.post("/items/", status_code = status.HTTP_201_CREATED,tags=["items"])
async def create_item(item: Item1):
    return item

@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]

# Tags with Enums

class Tags(Enum):
    items = "items"
    users = "users"


@app.get("/items/same_tag", tags=[Tags.items])
async def get_items():
    return ["Portal gun", "Plumbus"]


@app.get("/users/same_tags", tags=[Tags.users])
async def read_users():
    
    return ["Rick", "Morty"]    

# Summary and description

class Item2(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.post("/items/", response_model=Item2, response_description="The created item",summary="Create an item", tags=["summary"])
async def create_item(item: Item2):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item

# Deprecate a path operation

@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]