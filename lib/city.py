#!usr/bin/env python3
# coding: utf8

from base import Base
from sqlalchemy import Column, Integer, Float, String


class City(Base):
    __tablename__ = "cities"

    id         = Column(Integer, primary_key=True)
    city       = Column(String(50), nullable=False)
    city_ascii = Column(String(50), nullable=False)
    lat        = Column(Float, nullable=False)
    lng        = Column(Float, nullable=False)
    country    = Column(String(20), nullable=False)
    iso2       = Column(String(3), nullable=False)
    iso3       = Column(String(3), nullable=False)
    admin_name = Column(String(50), nullable=False)
    population = Column(Integer)
