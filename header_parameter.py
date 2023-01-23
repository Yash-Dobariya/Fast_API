# Header Parameters

from fastapi import FastAPI, Header, Path, Body, Query

app = FastAPI()

# Import Header

@app.get("/items/import_header")
async def read_items(user_agent: str | None = Header(default=None)):
    return {"User-Agent": user_agent}

# Declare Header parameters

@app.get("items/header_parameters")
def read_items(user_agent: str | None = Header(default=None)):
    return {"User-Agent": user_agent}

# Automatic conversion

@app.get("/items/automatic_conversion")
def read_items(stranger: str | None = Header(default = None, convert_underscores = True)):
    return{"strange_header": stranger}

# Duplicate Header

@app.get("/items/duplicate_header")
async def read_items(x_token: list[str] | None = Query(default=None)):
    return {"X-Token values": x_token}