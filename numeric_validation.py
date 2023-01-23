# Path Parameters and Numeric Validations
from fastapi import FastAPI, Path, Query

app = FastAPI()

# Import Path
# Declare metadata

@app.get("/items/{item_id}")
def read_items(item_id: int = Path(title="The ID of item too get"),
               q : str = Query(default=None, alias="item-query")):

    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# Order the parameters as you need

@app.get("/items/{item_id}/order_parameter")
def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# Order the parameters as you need, tricks

@app.get("/item/{item_id}/order_parameter_trick")
def read_items(*, item_id: int =Path(title="The id of the item to  get"),q: str):
    results ={"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# Number validations: greater than or equal

@app.get("/item/{item_id}/number_validation")
def read_item(*,item_id: int = Path(title = "The ID of the item to get", gt=0, le=1000),q:str):
    results={"item_id": item_id}
    if q:
        results.update({"q":q})
        return results

# Number validations: floats, greater than and less than

@app.get("/item/{item_id}")
def read_item(*,item_id: int =Path(title="The ID of the item to get",ge=0, le=10),q: str, size: float = Query(gt=0, lt=10.5)):
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    return results 

