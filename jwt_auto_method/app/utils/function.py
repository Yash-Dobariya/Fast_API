from datetime import datetime
from fastapi_jwt_auth import AuthJWT
from fastapi import status, Depends, HTTPException
from app.utils.token import get_config
from os import getenv
from jose import jwt, JWTError

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")  # should be kept secret
JWT_REFRESH_SECRET_KEY = getenv("JWT_REFRESH_SECRET_KEY")

def currenttime():
    return datetime.utcnow()

def authenticate(Authorize : AuthJWT = Depends([get_config])):
    try:
        Authorize.jwt_required()
        current_user =  Authorize.get_jwt_subject()
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid access Token 😢")


def decode_access_token(access_token: str) -> dict:
    try:
        decoded_token = jwt.decode(access_token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        if decoded_token["exp"] >= datetime.timestamp(datetime.now()):
            return decoded_token
        else:
            return {"type": "Error", "message": "Token is expired"}
    except JWTError:
        return {"type": "Error", "message": "Token is invalid"}