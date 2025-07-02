from sqlalchemy import Column, Integer, String
from db.sql import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    pwd_hash = Column(String)


