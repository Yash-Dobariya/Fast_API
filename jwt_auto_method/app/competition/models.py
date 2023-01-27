from app.database import Base
from sqlalchemy import Column, String, ForeignKey
from app.user.model import User
from app.utils.same_model import DBBaseModel
from app.user.model import User
import os

class CompetitionTable(Base, DBBaseModel):

    __tablename__ = 'competition_table'
    
    name = Column(String)
    status = Column(String)
    description = Column(String)
    created_by = Column(ForeignKey(User.id))