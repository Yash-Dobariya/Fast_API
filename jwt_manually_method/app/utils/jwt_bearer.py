from jose import JWTError, jwt
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from app.utils.token import decode_access_token
from os import getenv
from dotenv import load_dotenv
from app.user.model import User
from pydantic  import BaseModel

load_dotenv()

SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days

class TokenData(BaseModel):

    id : str


def get_user(user, id: str):
    if id in User:
        user_dict = User[id]
        return User(**user_dict)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("id")
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=id)
    except JWTError:
        raise credentials_exception
    user = get_user(User, id = token_data.id)
    if user is None:
        raise credentials_exception
    return user

# class JWTBearer(HTTPBearer):
#     def __init__(self, auto_error: bool = True):
#         super().__init__(auto_error=auto_error)

#     async def __call__(self, request: Request):
#         credentials: HTTPAuthorizationCredentials = await super().__call__(request)
#         if credentials:
#             if not credentials.scheme == "Bearer":
#                 raise HTTPException(
#                     status_code=403, detail="Invalid authentication scheme."
#                 )
#             if not self.verify_jwt(credentials.credentials):
#                 raise HTTPException(
#                     status_code=403, detail="Invalid token or expired token."
#                 )
#             return credentials.credentials
#         else:
#             raise HTTPException(status_code=403, detail="Invalid authorization code.")

#     def verify_jwt(self, jwtoken: str) -> bool:
#         try:
#             payload = decode_access_token(jwtoken)
#         except JWTError:
#             payload = None
#         isvalid = True if payload else False
#         return isvalid