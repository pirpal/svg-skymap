#!usr/bin/env python3
# coding: utf8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String

Base = declarative_base()

class DeepSkyObject(Base):
    __tablename__ = "deep_sky_objects"

    id          = Column(Integer, primary_key=True)
    ra          = Column(Float, nullable=False)
    dec         = Column(Float, nullable=False)
    dist        = Column(Float, nullable=False)
    const       = Column(String)
    mag         = Column(Float, nullable=False)
    name        = Column(String)
    rarad       = Column(Float, nullable=False)
    decrad      = Column(Float, nullable=False)
    r1          = Column(Float)
    r2          = Column(Float)
    angle       = Column(Float)
    dso_source  = Column(Integer)
    id1         = Column(Integer)
    cat1        = Column(String)
    id2         = Column(Integer)
    cat2        = Column(String)
    dupid       = Column(Integer)
    dupcat      = Column(String)
    display_mag = Column(Float)
