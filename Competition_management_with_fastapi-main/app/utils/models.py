from app.database.database import Base
from sqlalchemy import Column , Integer , String  , DateTime , Boolean , ForeignKey
from datetime import datetime
from app.utils.func import commonfuntime


class Commommodel():
    is_active = Column(Boolean,default=True )
    is_delete = Column(Boolean , default=False)
    created_at = Column(DateTime, default = commonfuntime())
    update_at = Column(DateTime , default = commonfuntime())
