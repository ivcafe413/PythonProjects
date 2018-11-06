import sys
import logging
import unittest
import timeit

from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from CollisionDetection.Algorithms import CollideRectTest
from CollisionDetection.Algorithms import BBSeparatingAxisTest as BBSAT
from CollisionDetection.Algorithms import AABBDetection as AABB

from GameObjects.TestGameObject import TestGameObject

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
#stream_handler = logging.StreamHandler(sys.stdout)
#logger.addHandler(stream_handler)

class CollisionDetectionTests(unittest.TestCase):
    def setUp(self):
        pass
    
    # pygame colliderect tests
    def test_collide_rect_test(self):
        """Greenlight test - two objects slightly intersecting"""
        obj1 = TestGameObject(100, 100, 20, 20)
        obj2 = TestGameObject(110, 100, 20, 20)

        self.assertTrue(CollideRectTest(obj1.bounds, obj2.bounds),
            "objects colliding return true")

    def test_not_colliding_rect_test(self):
        """Redlight - two objects adjacent, not colliding"""
        obj1 = TestGameObject(100, 100, 20, 20)
        obj2 = TestGameObject(120, 100, 20, 20)

        self.assertFalse(CollideRectTest(obj1.bounds, obj2.bounds),
            "objects not colliding, returns false")

    # Bounding-box separating axis tests
    def test_bbsat_colliding_x(self):
        obj1 = TestGameObject(100, 100, 20, 20)
        obj2 = TestGameObject(110, 100, 20, 20)

        self.assertTrue(BBSAT(obj1.bounds, obj2.bounds),
            "bbsat objects colliding x return true")

    def test_bbsat_colliding_y(self):
        obj1 = TestGameObject(100, 100, 20, 20)
        obj2 = TestGameObject(100, 110, 20, 20)

        self.assertTrue(BBSAT(obj1.bounds, obj2.bounds),
            "bbsat objects colliding y return true")

    def test_bbsat_colliding_both(self):
        obj1 = TestGameObject(100, 100, 20, 20)
        obj2 = TestGameObject(110, 110, 20, 20)

        self.assertTrue(BBSAT(obj1.bounds, obj2.bounds),
            "bbsat objects colliding diagonal return true")

    def test_bbsat_x_axis_gap(self):
        obj1 = TestGameObject(100, 100, 20, 20)
        obj2 = TestGameObject(125, 100, 20, 20)

        self.assertFalse(BBSAT(obj1.bounds, obj2.bounds),
            "bbsat objects x axis gap return false")

    def test_bbsat_y_axis_gap(self):
        obj1 = TestGameObject(100, 100, 20, 20)
        obj2 = TestGameObject(125, 100, 20, 20)

        self.assertFalse(BBSAT(obj1.bounds, obj2.bounds),
            "bbsat objects y axis gap return false")

    def test_bbsat_double_axis_gap(self):
        obj1 = TestGameObject(100, 100, 20, 20)
        obj2 = TestGameObject(125, 125, 20, 20)

        self.assertFalse(BBSAT(obj1.bounds, obj2.bounds),
            "bbsat objects x-y axis gap return false")

    # AABB collision tests
    def test_aabb_colliding_x(self):
        obj1 = TestGameObject(100, 100, 20, 20)
        obj2 = TestGameObject(110, 100, 20, 20)

        self.assertTrue(AABB(obj1.bounds, obj2.bounds),
            "aabb objects colliding x return true")

    def test_aabb_colliding_y(self):
        obj1 = TestGameObject(100, 100, 20, 20)
        obj2 = TestGameObject(100, 110, 20, 20)

        self.assertTrue(AABB(obj1.bounds, obj2.bounds),
            "aabb objects colliding y return true")

    def test_aabb_colliding_both(self):
        obj1 = TestGameObject(100, 100, 20, 20)
        obj2 = TestGameObject(110, 110, 20, 20)

        self.assertTrue(AABB(obj1.bounds, obj2.bounds),
            "aabb objects colliding diagonal return true")

    def test_aabb_x_axis_gap(self):
        obj1 = TestGameObject(100, 100, 20, 20)
        obj2 = TestGameObject(125, 100, 20, 20)

        self.assertFalse(AABB(obj1.bounds, obj2.bounds),
            "aabb objects x axis gap return false")

    def test_aabb_y_axis_gap(self):
        obj1 = TestGameObject(100, 100, 20, 20)
        obj2 = TestGameObject(125, 100, 20, 20)

        self.assertFalse(AABB(obj1.bounds, obj2.bounds),
            "aabb objects y axis gap return false")

    def test_aabb_double_axis_gap(self):
        obj1 = TestGameObject(100, 100, 20, 20)
        obj2 = TestGameObject(125, 125, 20, 20)

        self.assertFalse(AABB(obj1.bounds, obj2.bounds),
            "aabb objects x-y axis gap return false")

    # pygame collision timing tests
    def test_pygame_colliderect_timing(self):
        logger.debug("Collide Rect Test: %s sec.", timeit.timeit(stmt = "CollideRectTest(obj1.bounds, obj2.bounds)",
            setup="""\
from CollisionDetection.Algorithms import CollideRectTest
from GameObjects.TestGameObject import TestGameObject
obj1 = TestGameObject(100, 100, 20, 20)
obj2 = TestGameObject(125, 125, 20, 20)
            """))

    def test_pygame_bbsat_timing(self):
        logger.debug("BB Separating Axis Test: %s sec.", timeit.timeit(stmt = "BBSAT(obj1.bounds, obj2.bounds)",
            setup="""\
from CollisionDetection.Algorithms import BBSeparatingAxisTest as BBSAT
from GameObjects.TestGameObject import TestGameObject
obj1 = TestGameObject(100, 100, 20, 20)
obj2 = TestGameObject(125, 125, 20, 20)
            """))

    def test_pygame_basic_aabb_timing(self):
        logger.debug("Basic AABB Collision Test: %s sec.", timeit.timeit(stmt = "AABB(obj1.bounds, obj2.bounds)",
            setup="""\
from CollisionDetection.Algorithms import AABBDetection as AABB
from GameObjects.TestGameObject import TestGameObject
obj1 = TestGameObject(100, 100, 20, 20)
obj2 = TestGameObject(125, 125, 20, 20)
            """))

    def tearDown(self):
        # logger.removeHandler(stream_handler)
        pass

if __name__ == '__main__':
    unittest.main(exit=False)