from fastapi import FastAPI
from app.user.route import user_routes
from app.entry.route import entry
from app.competition.route import competition


app = FastAPI()

app.include_router(user_routes, tags=["User"])
app.include_router(entry, tags=["Entry"])
app.include_router(competition, tags=["Competition"])