#!/usr/bin/python3
""" relations database """

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """ class class """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))
