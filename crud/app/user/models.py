from app.database.database import Base
from sqlalchemy import Column, String, Integer, Date
from app.utils.same_model import DBBaseModel


class UserTable(Base, DBBaseModel):

    __tablename__ = "user_table"

    id = Column(Integer, primary_key = True, index = True, autoincrement= True)
    name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)