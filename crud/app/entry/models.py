from app.database.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey,  DateTime
from app.competition.models import CompetitionTable
from datetime import datetime


class EntryTable(Base):

    __tablename__ = 'entry_table'
    
    id = Column(Integer, primary_key = True, index = True, autoincrement =True)
    title = Column(String)
    topic = Column(String)
    state = Column(String)
    country = Column(String)
    competition_id = Column(Integer, ForeignKey(CompetitionTable.id))
    is_delete = Column(DateTime, default=datetime.utcnow())
    create_at = Column(DateTime, default=datetime.utcnow())
    update_at = Column(DateTime, default=datetime.utcnow())