import sys
import logging
import unittest
import time
import random

from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from GameObjects.TestGameObject import TestGameObject
from CollisionDetection.QuadTree import QuadTree
from CollisionDetection.Algorithms import CollideRectTest

class QuadTreeCollisionPerformanceTests(unittest.TestCase):
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()

    def setUp(self):
        self.quadTree = QuadTree(0, 0, 800, 600)
        self.gameObjects = []

        self.__startTime = time.time()

    def test_basic_quad_tree_performance(self):
        collisions = []
        for i in range(100):
            obj = TestGameObject(random.randint(0, 800), random.randint(0, 600), 20, 20)
            self.gameObjects.append(obj)
            self.quadTree.insert(obj)

        for o in self.gameObjects:
            collidables = self.quadTree.getCollidableObjects(o)
            if collidables:
                for c in collidables:
                    if CollideRectTest(o.bounds, c.bounds):
                        # Collision detected
                        collisions.append((o, c))

        print("Collisions: {}".format(len(collisions)))

    def tearDown(self):
        self.__elapsedTime = time.time() - self.__startTime
        print('{} ({}s)'.format(self.id(), round(self.__elapsedTime, 2)))

        self.quadTree = None
        self.gameObjects = None

if __name__ == '__main__':
    unittest.main(exit=False)