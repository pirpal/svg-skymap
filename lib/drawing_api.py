#!usr/bin/env python3

import svgwrite
from colors import *


class SvgSkyDrawer:
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

if __name__ == "__main__":
    drawer = SvgSkyDrawer({
        "name": "default",
        "theme": "default-dark"
    })
    
