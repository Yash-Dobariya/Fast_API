from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text

class Item(Base):   

    __tablename__ = 'items'
    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = True, unique = True)
    description = Column(Text)
    price = Column(Integer,nullable = True)
    on_offer = Column(Boolean, default = True)

    def __repr__(self) -> str:
        return f"<Item name={self.name} price={self.price}>"