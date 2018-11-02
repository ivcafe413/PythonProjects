import sys
import logging
import unittest

from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from CollisionDetection.QuadTree import QuadTree
from CollisionDetection.QuadTree import ObjectWithinBounds
from GameObject import GameObject

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

class QuadTreeTest(unittest.TestCase):
    def setUp(self):
        stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stream_handler)
        
        self.quadTree = QuadTree(0, 0, 800, 600)

    def test_insert_object_within_threshold(self):
        obj = GameObject(100, 100, 20, 20)
        #logger.debug("obj type {0} instance {1}".format(type(obj), isinstance(obj, GameObject)))
        self.quadTree.insert(obj)

        self.assertTrue(obj in self.quadTree.objects, "object in list")
        self.assertTrue(ObjectWithinBounds(obj, self.quadTree.bounds), "object in bounds")
    
    @unittest.expectedFailure
    def test_fail_insert_object_outside_threshold(self):
        obj = GameObject(1000, 1000, 20, 20)
        self.quadTree.insert(obj) # Should throw exception

    def test_get_collidables_without_self(self):
        """Test returning the list of collidables without returning self in the list so that self is not compared for collision"""
        selfObj = GameObject(100, 200, 20, 20)
        obj1 = GameObject(200, 300, 20, 20)
        obj2 = GameObject(300, 400, 10, 10)
        self.quadTree.insert(selfObj)
        self.quadTree.insert(obj1)
        self.quadTree.insert(obj2)

        # Checking selfObj against the QuadTree should only return the other 2 objs
        collidables = self.quadTree.getCollidableObjects(selfObj)
        self.assertTrue(len(collidables) == 2, "correct collidable count")
        self.assertTrue(selfObj not in collidables, "no self reference in collidables")

    def tearDown(self):
        stream_handler = logging.StreamHandler(sys.stdout)
        logger.removeHandler(stream_handler)

        self.quadTree = None

if __name__ == '__main__':
    unittest.main(exit=False)