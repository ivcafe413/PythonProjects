import pygame
import logging
import Config as c

from Game import Game
from Spawner import *
from Player import *
from UserEvents import *

class GameRunner(Game):
	def __init__(self):
		Game.__init__(self, c.screen_width, c.screen_height) #add config vars
		
		spawner = Spawner(400, 300, 30, 30, (128, 128, 128))
		self.state.objects.append(spawner)
		#self.event_handlers[SPAWN_ZOM].append(spawner.SpawnZom)
		
		player = Player(200, 200, 20, 20, (34, 139, 34), 2)
		self.state.objects.append(player)
		self.keydown_handlers[pygame.K_LEFT].append(player.handle_key)
		self.keydown_handlers[pygame.K_RIGHT].append(player.handle_key)
		self.keydown_handlers[pygame.K_UP].append(player.handle_key)
		self.keydown_handlers[pygame.K_DOWN].append(player.handle_key)

		self.keyup_handlers[pygame.K_LEFT].append(player.handle_key)
		self.keyup_handlers[pygame.K_RIGHT].append(player.handle_key)
		self.keyup_handlers[pygame.K_UP].append(player.handle_key)
		self.keyup_handlers[pygame.K_DOWN].append(player.handle_key)
		
def main():
	logging.basicConfig(level=logging.INFO)
	GameRunner().run()
	
if __name__ == '__main__':
	main()