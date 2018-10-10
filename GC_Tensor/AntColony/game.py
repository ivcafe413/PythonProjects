import sys
from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np

import pygame

class Game:
    def __init__(self, rows, cols):
        # Game State
        self.objects = []
        # self.agents = []
        self.surface = pygame.display.set_mode((800, 600))

    def update(self):
        # Game gives the object the state
        for o in self.objects:
            # spread = self.map.spread(o.position, self.radius)
            # state = None # TODO: get state spread
            state = None
            o.update(state)

    def render(self):
        self.surface.fill((222, 184, 135)) # burlywood
        
        for o in self.objects:
            o.draw(self.surface)
        
        pygame.display.update()