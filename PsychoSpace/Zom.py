import pygame
import Config as c

from random import *
from GameObject import GameObject

class Zom(GameObject):
	def __init__(self, x, y, w, h, color, special_effect=None):
		GameObject.__init__(self, x, y, w, h)
		self.color = color
		self.special_effect = special_effect
		
		self.idle_time = 0
		self.idle_bounds = (500, 1000)
		self.idle_rng = randint(min(self.idle_bounds), max(self.idle_bounds))
		self.speed = 1
		self.direction = randint(1, 4)
		
	def draw(self, surface):
		pygame.draw.rect(surface, self.color, self.bounds)
		
	def update(self, state):
		self.idle_time += state.UPDATE_MS_PF
		
		if(self.idle_time >= self.idle_rng):
			#Change direction
			self.direction = randint(1, 4)
			self.idle_rng = randint(min(self.idle_bounds), max(self.idle_bounds))
			self.idle_time -= self.idle_rng
		
		if self.direction == 1: #Left
			dx = -(min(self.speed, self.left))
		elif self.direction == 2: #Up
			dy = -(min(self.speed, self.top))
		elif self.direction == 3: #Right
			dx = min(self.speed, c.screen_width - self.right)
		elif self.direction == 4: #Down
			dy = min(self.speed, c.screen_height - self.bottom)
			
		if not 'dx' in vars():
			dx = 0
		if not 'dy' in vars():
			dy = 0
			
		self.move(dx, dy)