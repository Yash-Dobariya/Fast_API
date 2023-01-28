from jose import jwt
import jwt
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from os import getenv
from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):

    try:

        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    except jwt.exceptions.DecodeError:
        raise HTTPException(status_code=400, detail="Invalid token 😢")

    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="Token expired 😪")

    except jwt.exceptions.InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    user_id = decoded_token.get("user_id")

    return  user_id