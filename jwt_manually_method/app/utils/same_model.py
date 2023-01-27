from sqlalchemy import Column, Boolean, DateTime, String , ForeignKey  
from app.utils.function import currenttime
from sqlalchemy.dialects.postgresql import UUID
import uuid
import os

class DBBaseModel():

    id = Column(UUID(as_uuid = True), default = uuid.uuid4, primary_key=True)
    create_at = Column(DateTime, default = currenttime())
    update_at = Column(DateTime, default = currenttime())
    updated_by = Column(String, onupdate = os.getlogin())
    is_active = Column(Boolean, default = True) 