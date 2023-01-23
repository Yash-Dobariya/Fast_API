from sqlalchemy import Column, Integer, String
from database import Base

class Info(Base):

    __tablename__ = "info"

    id :Column(Integer, primary_key = True, unique = True)
    name : Column(String)
    enrollment_no : Column(Integer())
    course : Column(String)
    mobail_no : Column(Integer())
    address : Column (String(200))