from app.database.database import Base
from sqlalchemy import Column , Integer , String  , DateTime , Boolean , ForeignKey
from app.models.user_model import User
from datetime import datetime
from app.utils.models import Commommodel
#Model for competition table


class Competition(Base,Commommodel):
    __tablename__ = "competition_table"
    id = Column(Integer, primary_key = True,index = True)
    name = Column(String)
    status = Column(String)
    description = Column(String)
    user_id=Column(Integer,ForeignKey(User.id))
