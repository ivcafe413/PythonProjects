import sys
import logging
import unittest

from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from CollisionDetection.QuadTree import QuadTree
from CollisionDetection.QuadTree import ObjectWithinBounds
from GameObject import GameObject

class QuadTreeTest(unittest.TestCase):
    def setUp(self):
        self.quadTree = QuadTree(0, 0, 800, 600)

    def test_insert_object_within_threshold(self):
        obj = GameObject(100, 100, 20, 20)
        self.quadTree.insert(obj)

        self.assertTrue(obj in self.quadTree.objects, "object in list")
        self.assertTrue(ObjectWithinBounds(obj, self.quadTree.bounds), "object in bounds")
    
    @unittest.expectedFailure
    def test_fail_insert_object_outside_threshold(self):
        obj = GameObject(1000, 1000, 20, 20)
        self.quadTree.insert(obj) # Should throw exception

    def tearDown(self):
        self.quadTree = None

if __name__ == '__main__':
    unittest.main(exit=False)