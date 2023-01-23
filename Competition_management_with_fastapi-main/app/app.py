#Import all routes

from fastapi import FastAPI
from app.routes.competition_route import competition
from app.routes.entry_route import entry
from app.routes.user_route import userdata
from app.routes.count_route import counted

app = FastAPI()

app.include_router(competition)
app.include_router(entry)
app.include_router(userdata)
app.include_router(counted)
