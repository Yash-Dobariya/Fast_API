from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_ENGINE_URL = 'postgresql://postgres:1234@localhost/student_info_db'

engine = create_engine(DATABASE_ENGINE_URL)

SessionLocal = sessionmaker( autocommit=False, autoflush= False, bind=engine)

Base = declarative_base()