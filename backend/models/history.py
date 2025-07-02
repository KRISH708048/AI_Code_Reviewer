from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.sql import Base

class ReviewHistory(Base):
    __tablename__ = 'review_history'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    code_id = Column(String)  # Mongo ID reference
    created_at = Column(DateTime)
    title = Column(String)
    user = relationship("User")
