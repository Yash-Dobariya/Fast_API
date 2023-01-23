from sqlalchemy import Column, Boolean, DateTime
from app.utils.function import currenttime


class DBBaseModel():

    create_at = Column(DateTime, default = currenttime())
    update_at = Column(DateTime, default = currenttime())
    is_active = Column(Boolean, default = True)
    is_delete = Column(Boolean, default = False)