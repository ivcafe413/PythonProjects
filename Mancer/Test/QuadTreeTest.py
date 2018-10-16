import sys
import logging
import unittest

from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from QuadTree.QuadTree import QuadTree

class QuadTreeTest(unittest.TestCase):
    def setUp(self):
        self.quadTree = QuadTree(0, 0, 800, 600)

if __name__ == '__main__':
    unittest.main()