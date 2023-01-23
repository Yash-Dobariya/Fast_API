# Import Cookie

from fastapi import FastAPI, Cookie

# First import Cookie

app = FastAPI()

@app.get("/items")
def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}