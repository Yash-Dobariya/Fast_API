from jwt.password import hash_password, verify_password
from fastapi import APIRouter
from jwt.schema import User, Token
from jwt.model import User_db


route = APIRouter()

@route.post('/detail', response_model=Token)
async def sign_up(request: User):
    user = User_db(username = request.username, email = request.email, full_name = request.full_name)
    