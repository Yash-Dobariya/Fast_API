from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from os import getenv


load_dotenv()

DB_DRIVER = getenv("DB_DRIVER")
DB_USERNAME = getenv("DB_USERNAME")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_HOST = getenv("DB_HOST")
DB_PORT = getenv("DB_PORT")
DB_DATABASE = getenv("DB_DATABASE")


SQL_DATABASE_CONNECTION = f"{DB_DRIVER}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

engine = create_engine(SQL_DATABASE_CONNECTION)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try :
        yield db
    finally:
        db.close()
