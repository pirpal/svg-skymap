#!usr/bin/env python3
# coding: utf8

import tkinter as tk
import svgwrite
from base import Session
# from drawer import Drawer
from lib.star import Star
from lib.deep_sky_object import DeepSkyObject
from lib.city import City


class SvgSkymapsTk(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.geometry("800x400+50+0")
        self.title("SVG Skymaps")
        self.initUI()
        self.session = Session()
        self.getConstellationStars("Ori")

    def initUI(self):
        self.can = tk.Canvas(width=600, height=400, bg="#00031f")
        self.can.grid(row=0, column=0)

    def initConstellations(self):
        pass

    def getConstellationStars(self, const: str):
        """
        >>> getConstellationStars("Ori")
        """
        stars = self.session.query(Star) \
                            .filter(Star.con.ilike(const.lower()))
        return stars
    
    def getCitiesByCountry(self, country: str):
        pass

if __name__ == "__main__":
    app = SvgSkymapsTk(None)
    app.mainloop()
