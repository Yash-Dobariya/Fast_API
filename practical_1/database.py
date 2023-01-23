from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:1234@localhost/practical_1", pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(bind= engine )
Base  = declarative_base()
