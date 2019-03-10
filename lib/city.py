#!usr/bin/env python3
# coding: utf8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String

Base = declarative_base()

class City(Base):
    __tablename__ = "cities"

    id         = Column(Integer, primary_key=True)
    city       = Column(String, nullable=False)
    city_ascii = Column(String, nullable=False)
    lat        = Column(Float, nullable=False)
    lng        = Column(Float, nullable=False)
    country    = Column(String, nullable=False)
    iso2       = Column(String, nullable=False)
    iso3       = Column(String, nullable=False)
    admin_name = Column(String, nullable=False)
    population = Column(Integer)
