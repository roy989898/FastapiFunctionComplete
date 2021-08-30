from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from utils.db.database import Base


# class Blog(Base):
#     __tablename__ = 'blogs'
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     body = Column(String)
#     # user_id = Column(Integer, ForeignKey('users.id'))
#     # user: 'User' = relationship('User', back_populates="blogs")


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)
    name = Column(String, unique=True)
    # blogs: List[Blog] = relationship('Blog')
