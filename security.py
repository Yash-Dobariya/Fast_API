from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth_scheme1 = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/item")
def read_item(token: str = Depends(oauth_scheme1)):
    return {"token": token}