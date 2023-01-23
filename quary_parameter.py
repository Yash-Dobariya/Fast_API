""" get Method"""

from fastapi import FastAPI

app = FastAPI()

# quary parameter

fake_item_db =[{"item_name":"Foo"},{"item_name":"Bar"},{"item_name":"Baz"}]

@app.get("/items1")
def read_item(skip: int=0, limit: int=10):
    return fake_item_db[skip: skip + limit]

# optional parameter

@app.get("/items2")
def read_item(item_id: int | None = None , item_value: str | None = None):
    return {"item_id": item_id,"item_value": item_value}

#type conversion

@app.get("/items3")
async def read_item(item_id: str, item_value: str | None = None, short: bool = False):
    item = {"item_id": item_id,"item_value" : item_value}
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item

# Multiple path and query parameters

@app.get("/user/{user_id}/items/{items_id}")
def read_user_item(user_id: int , item_id: str, item_value: str | None = None, short: bool=False):
    item = {"owner_id": user_id, "item_id": item_id, "item_value" : item_value}
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item