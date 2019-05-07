import sys
import logging
import pygame

from collections import defaultdict

import Config as c
from Game import Game
from GameRenderer import GameRenderer
from Vagrant import Vagrant

# Game runner CONSTANTS
TARGET_FPS = 60
LOOP_MS_PF = (1 / TARGET_FPS) * 1000

class GameRunner:
	"""Game Runner wraps Game state and handles game loop management"""
	def __init__(self):
		pygame.init() #

		# Main game state object
		self.gameState = Game(c.screen_width, c.screen_height)

		# Game renderer
		self.gameRenderer = GameRenderer(self.gameState, c.screen_width, c.screen_height)

		# Event handlers
		self.keydown_handlers = defaultdict(list)
		self.keyup_handlers = defaultdict(list)

		# Game runner properties
		self.runnerClock = pygame.time.Clock()
		self.elapsedTime = 0
		
		# initial state setup
		player = Vagrant(400, 300, 20, 20, (128, 128, 128), 5)
		self.keydown_handlers[pygame.K_LEFT].append(player.handle)
		self.keydown_handlers[pygame.K_RIGHT].append(player.handle)
		self.keydown_handlers[pygame.K_UP].append(player.handle)
		self.keydown_handlers[pygame.K_DOWN].append(player.handle)

		self.keyup_handlers[pygame.K_LEFT].append(player.handle)
		self.keyup_handlers[pygame.K_RIGHT].append(player.handle)
		self.keyup_handlers[pygame.K_UP].append(player.handle)
		self.keyup_handlers[pygame.K_DOWN].append(player.handle)
		self.gameState.gameObjects.append(player)

	def handle_events(self):
		for event in pygame.event.get(): #To prevent OS from locking up
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
			elif event.type == pygame.KEYDOWN:
				for handler in self.keydown_handlers[event.key]:
					handler(event.key)
			elif event.type == pygame.KEYUP:
				for handler in self.keyup_handlers[event.key]:
					handler(event.key)
		
	def clockFrame(self):
		fps = self.runnerClock.get_fps()
		pygame.display.set_caption("FPS: {0:2f}".format(fps))
		self.runnerClock.tick(TARGET_FPS)

	def run(self):
		while True:
			self.elapsedTime += self.runnerClock.get_time()
			# if self.elapsedTime >= (self.RENDER_MS_PF):
			# --> Update Time
			
			self.handle_events() # --> Process event queue
			
			#possibility of variable update time frame to 'learn' and balance update speed real-time
			# if not self.state.paused:
			while self.elapsedTime >= LOOP_MS_PF:
				if(self.elapsedTime >= (LOOP_MS_PF * 2)):
					logging.warning("Lag Frame: {0:n} over {1:n}".format(self.elapsedTime - LOOP_MS_PF, LOOP_MS_PF))
				self.gameState.update() #TODO: Passing in update MS?
				self.elapsedTime -= LOOP_MS_PF
			# --> Determine time passed, run updates
			
			self.gameRenderer.render() #TODO: passing in leftover elapsed time over Render MS for % for render extrapolation
			self.clockFrame()
		
def main():
	#TODO: Set logging level based on config
	logging.basicConfig(level=logging.INFO)
	GameRunner().run()
	
if __name__ == '__main__':
	main()