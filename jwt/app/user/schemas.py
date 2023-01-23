from pydantic import BaseModel
from enum import Enum
import uuid

"""Signup User"""
class UserGender(str,Enum):

    Male = "Male"
    Female = "Female"
    Other = "Other"

class UserRole(str,Enum):

    Admin ="Admin"
    User = "User"

class SignupUser(BaseModel):

    name : str
    password : str
    first_name : str
    last_name : str
    email : str
    gender : UserGender
    role : UserRole



"""Response User """
class DisplayUser(BaseModel):

    id : uuid.UUID
    name :str
    first_name : str
    last_name : str
    email :str 
    gender : UserGender
    role : UserRole

    class Config: 
        orm_mode = True
        use_enum_values = True

"""Login User"""
class LoginUser(BaseModel):

    email : str
    password : str


class Setting(BaseModel):

    """secret key code : python terminal 
    import secrets 
    secrets.token_hex()"""
    
    authjwt_secret_key : str= '5727fc0a524b82cbf5d18a82bb51d6d03e29cdee187cb4b98d3609b2a195a3b1'
    authjwt_cookie_location : set = {'cookies'}
    authjwt_cookie_secure : bool = True
    authjwt_cookie_csrf_protect : bool = True
    authjwt_cookie_samesite : str = 'lax'

class EmailUser(BaseModel):

    email : str