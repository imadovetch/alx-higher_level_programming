#!/usr/bin/python3
""" Write a python file that contains the class definition
of a State and an instance Base = declarative_base() """

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
db = sqlalchemy


class State(Base):
    """ create table """
    __tablename__ = 'states'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
