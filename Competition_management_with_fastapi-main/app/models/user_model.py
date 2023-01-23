from app.database.database import Base
from sqlalchemy import Column , Integer , String  , DateTime , Boolean , Date
from datetime import datetime
from app.utils.models import Commommodel
#Model for user table


class User(Base , Commommodel):
    __tablename__ = "user_table"
    id = Column(Integer, primary_key = True,index = True, autoincrement=True)
    name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
