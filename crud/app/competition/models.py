from app.database.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from app.user.models import UserTable
from app.utils.same_model import DBBaseModel


class CompetitionTable(Base, DBBaseModel):

    __tablename__ = 'competition_table'

    id = Column(Integer, primary_key = True, index = True,autoincrement =  True)
    name = Column(String)
    status = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey(UserTable.id))