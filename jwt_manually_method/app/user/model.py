from app.database import Base
from sqlalchemy import  Column, String
from app.utils.same_model import DBBaseModel

class User(Base, DBBaseModel):

    __tablename__ = "user"


    name = Column(String)
    password = Column(String)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    gender =Column(String)
    role = Column(String)
