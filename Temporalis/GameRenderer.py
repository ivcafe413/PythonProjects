import pygame
import sys
import logging

class GameRenderer:
    def __init__(self, game, width, height):
        self.game = game
        pygame.display.init()
        self.screen = pygame.display.set_mode((width, height))

        # Surfaces/layers
        self.stage = pygame.surface.Surface((width, height))
        self.stage.convert()
        #self.stage.set_alpha()

        self.curtain = pygame.surface.Surface((width, height))
        self.curtain.convert_alpha()
        self.curtain.set_alpha(0)
        
    def draw(self):
        """"""
        self.stage.fill((34, 139, 34)) # Green
        for o in self.game.gameObjects:
            o.draw(self.stage)

    def render(self):
        """"""
        #self.screen.fill((34, 139, 34))
        self.draw()

        self.screen.blit(self.stage, (0, 0))
        self.screen.blit(self.curtain, (0, 0))
        pygame.display.update()