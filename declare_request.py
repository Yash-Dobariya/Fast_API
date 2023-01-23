# Declare Request Example Data

from fastapi import FastAPI,Body
from pydantic import BaseModel, Field

# Pydantic schema_extra 

app = FastAPI()

class Item1(BaseModel):
    name : str
    description : str | None = None
    price : float 
    tax : float | None = None

    class Config:
        schema_extra = {"example":{"name": "Foo",
                                   "description": "A very nice Item",
                                   "price": 35.4,
                                   "tax":3.2}}

@app.put("/items/{items_id}/schema_extra")
def update_item(item_id: int, item: Item1):
    results = {"item_id": item_id, "item": item}
    return results

# Field additional arguments

class Item2(BaseModel):
    name: str = Field(example="Foo")
    description: str | None = Field( example="A very nice item")
    price: float = Field(example=35.2)
    tax: float | None = Field(default=None, example=3.2)


@app.put("/items/{item_id}/additioal_arguments")
async def update_item(item_id: int, item: Item2):
    results = {"item_id": item_id, "item": item}
    return results

# Body with example

class Item3(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.put("/items/{item_id}/body_example")
async def update_item(iteam_id: int,
                      item: Item3=Body(example={"name":"Foo",
                                                "description":"A very nice Item",
                                                "price":35.2,
                                                "tax":3.2})):
    results = {"item_id": iteam_id, "item": item}
    return results

# Body with multiple examples

class Item4(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}/multiple_example")
async def update_item(*,item_id: int,item: Item4 = Body(
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price strings to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results