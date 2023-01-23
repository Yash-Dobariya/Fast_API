"""post Method"""

# create your data model

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):

    name : str
    price : int
    description : str | None = None
    tax : float | None = None

app = FastAPI()
list1= list()

@app.post("/items")
def create_item(items : Item):
    items_dict = items.dict()
    if items.tax:
        price_with_tax = items.price + items.tax
        items_dict.update({"price_with_tax": price_with_tax})
    return list1.append(items_dict)
    
# Request body + path parameters

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}