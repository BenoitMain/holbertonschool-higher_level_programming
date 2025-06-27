#!/usr/bin/python3

"""
Defines a City class and a Base instance for SQLAlchemy
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


# Create the Base instance
Base = declarative_base()


class City(Base):
    """State class for the cities table"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
