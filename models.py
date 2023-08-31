from sqlalchemy import Column, String, Integer
from database import Base


class Post(Base):
    __tablename__ = "blogpost"
    id = Column(Integer, primary_key=True, index=True)
    title: str = Column(String, unique=True, nullable=False)
    author: str = Column(String, unique=False, nullable=False)
    message: str = Column(String, unique=False, nullable=False)
