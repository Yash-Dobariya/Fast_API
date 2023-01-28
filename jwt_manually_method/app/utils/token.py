import jwt
from os import getenv
from typing import Any, Union
from datetime import datetime, timedelta
from jose import JWTError, jwt
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days

# This Function return generate token

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:

    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expires_delta, **dict(subject)}
    # to_encode = {"exp": expires_delta, "sub": str(subject)} # This method in first access sub 
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:

    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expires_delta, **dict(subject)}
    # to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def decode_access_token(access_token: str):

    try:
        decoded_token = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        if decoded_token["exp"] >= datetime.timestamp(datetime.now()):
            return decoded_token
        else:
            return {"type": "Error", "message": "Token is expired"}

    except JWTError:
        return {"type": "Error", "message": "Token is invalid"}