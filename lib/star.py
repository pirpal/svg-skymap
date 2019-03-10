#!usr/bin/env python3
# coding: utf8

from base import Base
from sqlalchemy import Column, Integer, Float, String


class Star(Base):
    __tablename__ = "stars"

    id           = Column(Integer, primary_key=True)
    hip          = Column(Integer, nullable=False)
    hd           = Column(Integer, nullable=False)
    hr           = Column(Integer, nullable=False)
    gl           = Column(Integer, nullable=False)
    bf           = Column(String(20))
    proper       = Column(String(20))
    ra           = Column(Float, nullable=False)
    dec          = Column(Float, nullable=False)
    dist         = Column(Float, nullable=False)
    pmra         = Column(Float, nullable=False)
    pmdec        = Column(Float, nullable=False)
    rv           = Column(Float)
    mag          = Column(Float, nullable=False)
    absmag       = Column(Float, nullable=False)
    spect        = Column(String(20))
    ci           = Column(Float, nullable=False)
    x            = Column(Float, nullable=False)
    y            = Column(Float, nullable=False)
    z            = Column(Float, nullable=False)
    vx           = Column(Float, nullable=False)
    vy           = Column(Float, nullable=False)
    vz           = Column(Float, nullable=False)
    rarad        = Column(Float, nullable=False)
    decrad        = Column(Float, nullable=False)
    pmrarad      = Column(Float, nullable=False)
    pmdecrad     = Column(Float, nullable=False)
    bayer        = Column(String(20))
    flam         = Column(Integer)
    con          = Column(String(3))
    comp         = Column(Integer)
    comp_primary = Column(Integer)
    base         = Column(String(20))
    lum          = Column(Float, nullable=False)
    var          = Column(String(20))
    var_min      = Column(Float)
    var_max      = Column(Float)

