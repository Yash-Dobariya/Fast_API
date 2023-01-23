# Body - Nested Models

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Item1(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None
    tags : list=[]

# List fields

@app.put("/items/{item_id}/list_fields")
def update_item(item_id: int, item: Item1):
    results = {"item_id": item_id, "item": item}
    return results

# Declare a list with a type parameter

class Item2(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.put("/items/{item_id}/with_parameter")
async def update_item(item_id: int, item: Item2):
    results = {"item_id": item_id, "item": item}
    return results

# Set types

class Item3(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.put("/items/{item_id}/set_field")
async def update_item(item_id: int, item: Item3):
    results = {"item_id": item_id, "item": item}
    return results

# Define a submodel

class Image1(BaseModel):
    url: str
    name: str


class Item4(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image1 | None = None


@app.put("/items/{item_id}/sub_model")
async def update_item(item_id: int, item: Item4):
    results = {"item_id": item_id, "item": item}
    return results

# Special types and validation

class Image2(BaseModel):
    url: HttpUrl
    name: str

class Item5(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image2 | None = None


@app.put("/items/{item_id}/special_validation")
async def update_item(item_id: int, item: Item5):
    results = {"item_id": item_id, "item": item}
    return results

# Attributes with lists of submodels

class Image3(BaseModel):
    url: HttpUrl
    name: str


class Item6(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image3] | None = None


@app.put("/items/{item_id}/attribute_list")
async def update_item(item_id: int, item: Item6):
    results = {"item_id": item_id, "item": item}
    return results

# Deeply nested models

class Image4(BaseModel):
    url: HttpUrl
    name: str


class Item7(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image4] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item7]


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer