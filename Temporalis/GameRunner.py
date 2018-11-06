import sys
import logging
import pygame

from pygame.locals import *

import Config as c

from Game import Game
from GameRenderer import GameRenderer
from EventHandler import EventHandler
from Player import Player
from Trigger import Trigger

from Constants.EventHandlerConstants import *

# Game runner CONSTANTS
TARGET_FPS = 60
LOOP_MS_PF = (1 / TARGET_FPS) * 1000

class GameRunner:
	"""Game Runner wraps Game state and handles game loop management"""
	def __init__(self):
		logging.basicConfig(level=logging.DEBUG)
		pygame.init()

		# Main game state object
		self.gameState = Game(c.screen_width, c.screen_height)

		# Game renderer
		self.gameRenderer = GameRenderer(self.gameState, c.screen_width, c.screen_height)

		# Event Handler
		self.eventHandler = EventHandler(self.gameState)

		# Game runner properties
		self.runnerClock = pygame.time.Clock()
		self.elapsedTime = 0
		
		# initial state setup
		player1 = Player(400, 300, 20, 20, (128, 128, 128), 5)
		self.gameState.gameObjects.append(player1)

		# initial battle trigger setup
		trigger = Trigger(200, 300, 20, 20, (0, 0, 0))
		self.gameState.gameObjects.append(trigger)

		# Event register initial state
		self.eventHandler.configure_handlers(TOWN_NAV)
		
	def clockFrame(self):
		fps = self.runnerClock.get_fps()
		pygame.display.set_caption("FPS: {0:2f}".format(fps))
		self.runnerClock.tick(TARGET_FPS)

	def run(self):
		while True:
			self.elapsedTime += self.runnerClock.get_time() # Time since last tick
			
			# possibility of variable update time frame to 'learn' and balance update speed real-time
			# if not self.state.paused:
			while self.elapsedTime >= LOOP_MS_PF: # lag > time per update
				if(self.elapsedTime >= (LOOP_MS_PF * 2)): # if multiple update frames this times
					logging.warning("Lag Frame: {0:n} over {1:n}".format(self.elapsedTime - (LOOP_MS_PF * 2), LOOP_MS_PF * 2))
				self.eventHandler.handle_events()
				self.gameState.update() #TODO: Passing in update MS?
				
				self.elapsedTime -= LOOP_MS_PF # decrement the lag
			
			self.gameRenderer.render() #TODO: passing in leftover elapsed time over Render MS for % for render extrapolation
			self.clockFrame()
		
def main():
	#TODO: Set logging level based on config
	#logging.basicConfig(level=logging.INFO)
	GameRunner().run()
	
if __name__ == '__main__':
	main()