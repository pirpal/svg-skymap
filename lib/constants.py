#!usr/bin/venv python3
# coding: utf8

from math import pi
import pendulum
from datetime import datetime

"""
Most of units and constants used are taken from the book:
"Cosmographie:
 Comprendre les mouvements du Soleil, de la
 Lune et des planètes",
 by Denis Savoie.
 (Editions Belin Pour la Science)
"""
#---------------------------------------------------------------------
# Earth parameters
#---------------------------------------------------------------------
EARTH_EQUATORIAL_RADIUS = 6.3781363e6 # e = 6,378,136.3 meters
EARTH_POLAR_RADIUS      = 6.3567516e6 # p = 6,356,751.6 meters
EARTH_FLATTENING_RATIO  = 1 / 298.257 # f = (e - p) / e

#---------------------------------------------------------------------
# Time constants
#---------------------------------------------------------------------
SIDERAL_YEAR = 365.256366   # Earth revolution period in days

ANOMALISTIC_YEAR = 365.2596 # average days between two passages of
                            # Earth at its perihelion

JULIAN_YEAR = 365.25        # Year value in Julian calendar

#---------------------------------------------------------------------
# Physic constants
#---------------------------------------------------------------------
LIGHT_SPEED = 2.99792458e8 # 299 792 458 meters/second in space void

