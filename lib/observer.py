#!usr/bin/env python3
# coding: utf8

import pendulum

class Observer:
    def __init__(self, local_time: str, position: tuple, place_name: str):
        """
        local_time str format()
        For an observer positionned:
        - on Earth's equator
        - on Greenwich meridian
        - at OhOO J2000
        =>
        o = Observer("2000-1-1:00:00:00GMT+0", (0, 0), "Equator - Greenwich")
        """
