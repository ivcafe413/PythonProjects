from abc import abstractmethod
from GameObjects.GameObject import GameObject

class Moveable(GameObject):
    @abstractmethod
    def __init__(self, x, y, w, h, speed=(0,0)):
        super().__init__(x, y, w, h)
        self.speed = speed

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    @property
    def moving(self):
        return self.moving_left or self.moving_right or self.moving_up or self.moving_down

    def move(self, dx, dy):
        self.bounds = self.bounds.move(dx, dy)