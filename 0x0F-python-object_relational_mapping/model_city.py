#!/usr/bin/python3
""" This class is defines the State class """


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)
class City(Base):
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
