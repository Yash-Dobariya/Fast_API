from pydantic import BaseModel
from typing import Optional
import uuid
from dotenv import load_dotenv
import os

load_dotenv()

"""Signup User"""

class SignupUser(BaseModel):

    name : str
    password : str
    first_name : str
    last_name : str
    email : str
    gender : str
    role : Optional[str]= "User"



"""Response User """
class DisplayUser(BaseModel):


    name :str
    first_name : str
    last_name : str
    email :str 
    gender : str
    role : str


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
    
    authjwt_secret_key : str= os.getenv('SECRET_KEY')

