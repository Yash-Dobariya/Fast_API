from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

ENGINE_CONNECTION_URL = 'postgresql://postgres:yash@localhost:5432/compitition_database'

engine = create_engine(ENGINE_CONNECTION_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()