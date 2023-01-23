from app.database.database import Base
from sqlalchemy import Column , Integer , String  , DateTime , Boolean , ForeignKey
from app.models.competition_model import Competition
from datetime import datetime
#Model for entry table


class Entry_Table(Base):
    __tablename__ = "entry_table"
    id = Column(Integer, primary_key = True,index = True)
    title = Column(String)
    topic = Column(String)
    state = Column(String)
    country = Column(String)
    is_delete = Column(Boolean ,default=False)
    created_at = Column(DateTime, default= datetime.utcnow)
    updated_at = Column(DateTime, default= datetime.utcnow)
    competition_id = Column(Integer , ForeignKey(Competition.id))
