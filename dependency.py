# function in dependency

from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/function_dependency1")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/function_dependency2")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons

# Classes as Dependencies

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class CommonQueryParams1:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/class_dependency1")
async def read_items(commons: CommonQueryParams1 = Depends(CommonQueryParams1)):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams2:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/class_dependency2")
def read_items(commons: CommonQueryParams2 = Depends()):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response

# Sub-dependencies

def query_extractor(q: str | None = None):
    return q

def query_or_cookie_extractor(q: str = Depends(query_extractor), last_query: str | None = None):
    return {"q": q, "last_query": last_query}

@app.get("/item/sub_dependancy")
def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}

# Dependency in path

def verify_token(x_roken: str = Header()):
    if x_roken != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key

@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]