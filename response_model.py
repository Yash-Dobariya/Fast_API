from fastapi import FastAPI, Query, Header, Body, Path
from pydantic import BaseModel, EmailStr

app = FastAPI()

class Item1(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] 


@app.post("/items/")
async def create_item(item: Item1):
    return {"item":item}

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

# Don't do this in production!
@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user

# Response Model encoding parameters

class Item2(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item2, response_model_exclude_unset=False)
async def read_item(item_id: str):
    return items[item_id]

# Use the response_model_exclude_unset parameter

class Item3(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
    "/items/{item_id}/name",
    response_model=Item3,
    response_model_include=["name", "description"],
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item3, response_model_exclude=["tax"])
async def read_item_public_data(item_id: str):
    return items[item_id]
