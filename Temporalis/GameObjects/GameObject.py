from pygame.rect import Rect
from abc import ABC, abstractmethod
 
class GameObject(ABC):
    @abstractmethod
    def __init__(self, x, y, w, h):
        self.bounds = Rect(x - w/2, y - h/2, w, h) # Center on (x,y)
 
    @property
    def left(self):
        return self.bounds.left
 
    @property
    def right(self):
        return self.bounds.right
 
    @property
    def top(self):
        return self.bounds.top
 
    @property
    def bottom(self):
        return self.bounds.bottom
 
    @property
    def width(self):
        return self.bounds.width
 
    @property
    def height(self):
        return self.bounds.height
 
    @property
    def center(self):
        return self.bounds.center
 
    @property
    def centerx(self):
        return self.bounds.centerx
 
    @property
    def centery(self):
        return self.bounds.centery
 
    @abstractmethod
    def draw(self, surface):
        """"""
        pass
    
    @abstractmethod
    def update(self):
        """"""
        pass