from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker, declarative_base


URL_DATABASE = 'postgresql://postgres:yash@localhost:5432/demo'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()