#!usr/bin/env python3
# coding: utf8

import svgwrite
from colors import *


class Drawer:
    def __init__(self, args: dict):
        self.name = args["name"]
        self.theme = THEMES[args["theme"]]

    def defaultSolarSystem(self, paper_format: dict):
        """
        top view of solar system with false objects
        size / distance ratio but with correct orbital
        positions for given time and position
        defaultScene(A4_LANDSCAPE)
        """
        pass


    def HemisphericProjection(self, paper_format: dict):
        pass

    def testDrawConst(const: str):
        pass


