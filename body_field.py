from fastapi import FastAPI, Body
from pydantic import BaseModel,Field

app =FastAPI()

class Item(BaseModel):
    name: str
    desceription: str | None = Field(default=None, title="The description of the item", max_length = 300)
    price: float = Field(gt=0,description="The price must be greater than zero")
    tax: float | None = None

# Import Field

@app.put("/items/{item_id}/import_field")
def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results