from app.database import Base
from sqlalchemy import Column, String, ForeignKey
from app.competition.models import CompetitionTable
from app.utils.same_model import DBBaseModel
import os
from app.competition.models import CompetitionTable


class EntryTable(Base, DBBaseModel):

    __tablename__ = 'entry_table'   

    title = Column(String)
    topic = Column(String)
    state = Column(String)
    country = Column(String)
    created_by = Column(ForeignKey(CompetitionTable.id))