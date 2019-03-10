#!usr/bin/env python3
# coding: utf8

from constants import *

# --------------------------------------------------------------------
# Time functions
# --------------------------------------------------------------------

def getDayDuration():
    pass

def translateToEpochJ2000(lat: float, lng: float):
    """
    translateToEpochJ2000(float, float) -> (float, float)
    # coordinates for Bordeaux, France
    >>> translateToEpochJ2000(44.8500, -0.5950)
    (TODO, TODO)
    """
    # TODO
    pass

def timeToDecimalHours(h: int, m: int, s: int):
    """
    timeToDecimalHours(int, int, int) -> float
    >>> timeToDecimalHours(2, 15, 59)
    2.266388888888889 # hours
    """
    return h + (m * 1/60) + (s * 1/3600)

def timeToDecimalMinutes(h: int, m: int, s: int):
    """
    timeToDecimalMinutes(int, int, int) -> float
    >>> timeToDecimalMinutes(2, 15, 59)
    135.98333333333332 # minutes
    """
    return (h * 60) + m + (s * 1 / 60)

def timeToDecimalSeconds(h: int, m: int, s: int):
    """
    timeToDecimalMinutes(int, int, int) -> int
    >>> timeToDecimalSeconds(2, 15, 59)
    8159 # seconds
    """
    return int((h * 3600) + (m * 60) + s)


def calcEasterDay(year: int):
    """
    easter day:
    First sunday after full moon coming after each march 21st
    """
    pass

# --------------------------------------------------------------------
# Trigonometry functions
# --------------------------------------------------------------------
def degreesToAzimut(degrees: float):
    """
    degreesToAzimut(float) -> float
    >>> degreesToAzimut(-
    """
    pass

# --------------------------------------------------------------------
# Eclipses
# --------------------------------------------------------------------
