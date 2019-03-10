#!usr/bin/env python3

# Base for sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///db/skymaps.db")
Session = sessionmaker(bind=engine)

Base = declarative_base()
