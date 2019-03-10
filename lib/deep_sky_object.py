#!usr/bin/env python3
# coding: utf8

from base import Base
from sqlalchemy import Column, Integer, Float, String


class DeepSkyObject(Base):
    __tablename__ = "deep_sky_objects"

    id          = Column(Integer, primary_key=True)
    ra          = Column(Float, nullable=False)
    dec         = Column(Float, nullable=False)
    dist        = Column(Float, nullable=False)
    const       = Column(String(3))
    mag         = Column(Float, nullable=False)
    name        = Column(String(20))
    rarad       = Column(Float, nullable=False)
    decrad      = Column(Float, nullable=False)
    r1          = Column(Float)
    r2          = Column(Float)
    angle       = Column(Float)
    dso_source  = Column(Integer)
    id1         = Column(Integer)
    cat1        = Column(String(8))
    id2         = Column(Integer)
    cat2        = Column(String(8))
    dupid       = Column(Integer)
    dupcat      = Column(String(8))
    display_mag = Column(Float)
