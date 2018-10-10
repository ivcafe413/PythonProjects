import pygame
import logging
import Config as c

from random import *
from collections import defaultdict

from GameObject import GameObject
from Zom import Zom
from UserEvents import *

class Spawner(GameObject):
	def __init__(self, x, y, w, h, color):
		GameObject.__init__(self, x, y, w, h)
		self.color = color
		self.elapsedTime = 0
		self.spawn_interval = 1 #1 spawn per second
		self.spawn_ms = self.spawn_interval * 1000
		
		self.allow_spawn = True
		#pygame.time.set_timer(SPAWN_ZOM, 1000)
		
	def draw(self, surface):
		pygame.draw.rect(surface, self.color, self.bounds)
		
	def update(self, state):
		#Time
		self.elapsedTime += state.UPDATE_MS_PF
		
		if self.elapsedTime >= (self.spawn_ms):
			#pygame.event.post(pygame.event.Event(SPAWN_ZOM))
			self.spawnZom(state)
			self.elapsedTime -= (self.spawn_ms)
			
	def spawnZom(self, state):
		result = defaultdict(list)
		# rX = randint(1, c.screen_width)
		# rY = randint(1, c.screen_height)
		rX = self.centerx
		rY = self.centery
		state.objects.append(Zom(rX, rY, 10, 10, (170, 1, 20)))
		# result["object"] = Zom(rX, rY, 10, 10, (170, 1, 20))
		# result["createObject"] = True
		# return result