import pygame
import logging

from pygame.locals import *
from collections import defaultdict

from Player import Player
from Constants.UserEvents import *
from CollisionDetection.CollisionHandler import CollisionHandler

def __town_navigation_handler_configuration__(self):
    player = self.game.get(Player)
    if not player:
        raise Exception("No player object to key bind to")

    #logging.debug(type(player))
    player1 = next(player, None)
    if not player1:
        raise Exception("No player object to key bind to")

    # Keydown handling
    self.keydown_handlers[K_LEFT].append(player1.handle)
    self.keydown_handlers[K_RIGHT].append(player1.handle)
    self.keydown_handlers[K_UP].append(player1.handle)
    self.keydown_handlers[K_DOWN].append(player1.handle)
    
    # Keyup handling
    self.keyup_handlers[K_LEFT].append(player1.handle)
    self.keyup_handlers[K_RIGHT].append(player1.handle)
    self.keyup_handlers[K_UP].append(player1.handle)
    self.keyup_handlers[K_DOWN].append(player1.handle)

    # Event handling
    self.event_handlers[COLLISION].append(CollisionHandler)

__switcher__ = {
    1: __town_navigation_handler_configuration__
}

class EventHandler:
    def __init__(self, game):
        self.game = game

        # Event handlers
        self.handler_configurations = defaultdict(list)

        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.event_handlers = defaultdict(list)

        # Default state
        # self.get_handler_configuration(TOWN_NAV)

    def clear_handlers(self):
        self.keydown_handlers.clear()
        self.keyup_handlers.clear()
        self.event_handlers.clear()

    def get_handler_configuration(self, arg):
        func = __switcher__.get(arg, None)
        return func(self)

    def configure_handlers(self, state):
        self.clear_handlers()
        self.get_handler_configuration(state)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                raise SystemExit
            elif event.type == KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == KEYUP:
                for handler in self.keyup_handlers[event.key]:
                    handler(event.key)
            elif event.type == COLLISION:
                for handler in self.event_handlers[COLLISION]:
                    handler(event.game, event.obj1, event.obj2)