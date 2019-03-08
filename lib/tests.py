#!usr/bin/env python3

import unittest
from constants import *
from maths_api import *


class ConstantsTests(unittest.TestCase):
    def testEarthFlatteningRatio(self):
        e = EARTH_EQUATORIAL_RADIUS
        p = EARTH_POLAR_RADIUS
        flat_ratio = (e - p) / p
        self.assertEqual(
            round(EARTH_FLATTENING_RATIO, 4),
            round(flat_ratio, 4)
        )
        self.assertEqual(
            round(1 / 298.257, 6),
            round(EARTH_FLATTENING_RATIO, 6)
        )
        # difference between equatorial and polar radius is approx. 21 km
        self.assertEqual(
            int(EARTH_EQUATORIAL_RADIUS * EARTH_FLATTENING_RATIO / 1_000),
            21
        )


class TimeFunctionsTests(unittest.TestCase):
    def test_timeToDecimalHours(self):
        self.assertEqual(
            round(timeToDecimalHours(11, 37, 59), 3),
            11.633
        )
        self.assertEqual(
            round(timeToDecimalMinutes(11, 37, 59), 4),
            697.9833
        )
        self.assertEqual(
            timeToDecimalSeconds(11, 37, 59),
            41879
        )

        
        
# --------------------------------------------------------------------
if __name__ == "__main__":
    unittest.main()
