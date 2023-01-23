from fastapi import APIRouter

counted = APIRouter()

@counted.get("/count",tags=['count'])
def totalcount():

    return "total count is: "
