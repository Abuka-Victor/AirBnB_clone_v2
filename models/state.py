#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of State class
    args:
        __tablename___(str): Name of the table
        id (Integer): unique identifier of table's row
        name (String): name of states
        cities (Integer): State-City relationship
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='states',
                          cascade='all delete delete-orphan')
