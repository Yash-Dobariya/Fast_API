from app.user.route import user_routes
from fastapi import FastAPI

app = FastAPI()

app.include_router(user_routes)