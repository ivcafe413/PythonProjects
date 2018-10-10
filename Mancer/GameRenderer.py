import pygame
import sys
import logging

class GameRenderer:
    def __init__(self, game, width, height):
        self.game = game
        self.screen = pygame.display.set_mode((width, height))

    def draw(self):
        for o in self.game.gameObjects:
            o.draw(self.screen)

    def render(self):
        self.screen.fill((34, 139, 34)) #render function
        self.draw()
        pygame.display.update()