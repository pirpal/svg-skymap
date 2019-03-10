#!usr/bin/env python3
# coding: utf8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String

Base = declarative_base()

class Star(Base):
    __tablename__ = "stars"

    id           = Column(Integer, primary_key=True)
    hip          = Column(Integer, unique=True, nullable=False)
    hd           = Column(Integer, Unique=True, nullable=False)
    hr           = Column(Integer, Unique=True, nullable=False)
    gl           = Column(Integer, Unique=True, nullable=False)
    bf           = Column(String(50))
    proper       = Column(String(50))
    ra           = Column(Float, nullable=False)
    dec          = Column(Float, nullable=False)
    dist         = Column(Float, nullable=False)
    pmra         = Column(Float, nullable=False)
    pmdec        = Column(Float, nullable=False)
    rv           = Column(Float)
    mag          = Column(Float, nullable=False)
    absmag       = Column(Float, nullable=False)
    spect        = Column(String)
    ci           = Column(Float, nullable=False)
    x            = Column(Float, nullable=False)
    y            = Column(Float, nullable=False)
    z            = Column(Float, nullable=False)
    vx           = Column(Float, nullable=False)
    vy           = Column(Float, nullable=False)
    vz           = Column(Float, nullable=False)
    rarad        = Column(Float, nullable=False)
    radec        = Column(Float, nullable=False)
    pmrarad      = Column(Float, nullable=False)
    pmdecrad     = Column(Float, nullable=False)
    bayer        = Column(String)
    flam         = Column(Integer)
    con          = Column(String)
    comp         = Column(Integer)
    comp_primary = Column(Integer)
    base         = Column(String)
    lum          = Column(Float, nullable=False)
    var          = Column(String)
    var          = Column(Float)
    var          = Column(Float)
