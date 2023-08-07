import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

class User(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    firstname = Column(String(255))
    lastname = Column(String(255))
    email = Column(String(255), unique=True, nullable=False)

class Favorites(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    url = Column(String(255))
    user_id = Column(Integer, ForeignKey('user.id'))

class Comment(Model):
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Post(Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

class Media(Model):
    id = Column(Integer, primary_key=True)
    type = Column(String(50))  # You might want to use an Enum here
    url = Column(String(255), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))

class Planets(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    url = Column(String(255))

class Characters(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    url = Column(String(255))
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
