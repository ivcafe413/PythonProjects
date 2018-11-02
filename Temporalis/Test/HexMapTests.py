import unittest

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from HexMap.HexMap import HexMap

class HexMapTest(unittest.TestCase):
    def setUp(self):
        self.hexMap = HexMap(10, 10, 10)

    def test_coordinates_setup(self):
        self.assertEqual(len(self.hexMap.coordinates), 100)

if __name__ == '__main__':
    unittest.main()