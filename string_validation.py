"""Query Parameters and String Validations"""

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items")
def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Additional validation

@app.get("/items/add_validation")
def read_items(q: str  = Query(default=None, max_length=10)):
    result = {"items":[{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result

# Add more validations

@app.get("/items/add_more_validation")
def read_items(q: str | None = Query(default=None, min_length=3, max_length=10)):
    result = {"items":[{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result

# Add regular expressions

@app.get("/items/add_regular_expression")
async def read_items(q: str = Query(default=None, min_length=3, max_length=50, regex="^fixedquery$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Default values

@app.get("/items/default_values")
async def read_items(q: str = Query(default="fixedquery", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Make it required

@app.get("/items/make_it_required")
async def read_items(q: str = Query(min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Required with Ellipsis

@app.get("/items/ellipsis")
async def read_items(q: str = Query(default=..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Use Pydantic's Required instead of Ellipsis (...)

from pydantic import Required
@app.get("/items/required")
async def read_items(q: str = Query(default=Required, min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Query parameter list / multiple values

@app.get("/items/multiple_value")
async def read_items(q: list[str] | None = Query(default=None)):
    query_items = {"q": q}
    return query_items

# Query parameter list / multiple values with defaults

@app.get("/items/multiple_value_with_default")
async def read_items(q: list[str] = Query(default=[" ", "bar"])):
    query_items = {"q": q}
    return query_items

# Declare more metadata

@app.get("/items/more_metadata")
async def read_items(q: str = Query(default=None, title="Query string", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Alias parameters

@app.get("/items/alias_parameter")
async def read_items(q: str = Query(default=None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Exclude from OpenAPI

@app.get("/items/exclude_openapi")
async def read_items(hidden_query: str | None = Query(default=None, include_in_schema=False)):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}