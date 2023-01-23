from fastapi import FastAPI

app = FastAPI()

@app.get("/api/hello")
def say_hello():

    return 'Hello'

@app.get("/api/me")
def say_hello_me(name:str): 

    response = "hello " + name
    return response