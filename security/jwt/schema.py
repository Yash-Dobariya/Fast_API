from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):

    access_token : str
    token_type : str

class TokenData(BaseModel):

    username : Optional[str]

class User(BaseModel):
    username : str
    email : Optional[str]
    full_name : Optional[str]

class UserInDB(User):

    hashed_password: str
    