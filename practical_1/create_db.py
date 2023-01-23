from database import Base, engine
from models import Item

Base.metadata.create_all(engine)