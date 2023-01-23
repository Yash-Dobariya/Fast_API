from app.database import Base
from sqlalchemy import  Column, String, Enum, Date
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

class User(Base):

    __tablename__ = "user"

    id = Column(UUID(as_uuid = True), default = uuid.uuid4, primary_key=True)
    name = Column(String)
    password = Column(String)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    gender =Column(Enum("Male","Female","Other"))
    role = Column(Enum("Admin","User"))
    is_create = Column(Date, default = datetime.utcnow())
    is_update = Column(Date, default = datetime.utcnow())
    is_delete = Column(Date, default = datetime.utcnow())