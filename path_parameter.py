from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/user/me")
def read_user_me():
    return {"user id" : "the current user"}

@app.get("/item/{itemid}")  #path parameter
def read_item(itemid : int):
    return {"item_id": itemid}

@app.get("/item") # quary parameter
def read_item(number : int , text : str):
    return {"number " : number, "text " : text}

@app.get("/users")
def read_user_one():
    return ["yah", "dobariya"]

@app.get("/users")
def read_user_two():
    return ["dobariya", "yash"]

class ModelName(str, Enum):
    BScIT = "Computer Course"
    BBA = "Managment Course"
    CA = "Account Course"

@app.post("/models/")

def get_model(model_name:ModelName):
    if model_name == "Computer Course":
        return{"model_name":model_name, "message":"All computer languages"}

    elif model_name.value == "Managment Course":
        return {"model_name": model_name, "message": "Managment Course in business about to learn"}

    elif model_name == "Account Course":
        return {"model_name":model_name, "message": "all account to handle"}