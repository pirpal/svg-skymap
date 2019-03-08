#!usr/bin/env python3
# coding: utf8

A4_PORTRAIT  = {"w": 595, "h": 842}
A4_LANDSCAPE = {"w": 842, "h": 595}
A5_PORTRAIT  = {"w": 420, "h": 595}
A5_LANDSCAPE = {"w": 595, "h": 420}

PALETTE = {
    "nightblue":    "#29203a",
    "santorinblue": "#236fb3",
    "ghostwhite":   "#fff6f0",
    "orangebrick":  "#ff7318",
    "flashgreen":   "#0feb0f",
    "mediumyellow": "#ffda10",
    "redbrick":     "#f43c2e",
    "blackhole":    "#030301",
    "pastelpurple": "#b864c4",
}

THEMES = {
    "default-dark": {
        "background":  PALETTE["nightblue"],
        "ecliptic":    PALETTE["orangebrick"],
        "stars":       PALETTE["ghostwhite"],
        "star-tag":    PALETTE["santorinblue"],
        "messier-tag": PALETTE["pastelpurple"],
        "const-tag":   PALETTE["mediumyellow"] 
    },
    # TODO: default-light
}
