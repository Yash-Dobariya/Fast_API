from fastapi import FastAPI
from app.user.route import user
from app.competition.route import competition
from app.entry.route import entry

app = FastAPI()

app.get
app.include_router(user, tags="User")
app.include_router(competition, tags="Competition")
app.include_router(entry, tags="Entry")