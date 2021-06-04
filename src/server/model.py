from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from flask_login import UserMixin

import json

DeclarativeBase = declarative_base()

class Templates(DeclarativeBase):
    __tablename__ = "templates"

    id = Column('id', Integer, primary_key=True)
    title = Column('title', String)
    path = Column('path', String)
    desc = Column('desc', String)
    author = Column('author', String)

    def __init__(self, title, path, desc, author):
        self.title = title
        self.path = path
        self.desc = desc
        self.author = author


class Users(UserMixin, DeclarativeBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))

if __name__ == '__main__':
    engine = create_engine('sqlite:///db.sqlite')
    DeclarativeBase.metadata.create_all(engine)