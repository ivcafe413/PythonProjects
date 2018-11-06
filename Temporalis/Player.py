import pygame
from pygame.locals import *

import Config as c
from GameObject import GameObject

class Player(GameObject): #Subclass definition
	def __init__(self, x, y, w, h, color, speed):
		GameObject.__init__(self, x, y, w, h)
		self.color = color
		self.speed = speed
		self.moving_left = False
		self.moving_right = False
		self.moving_up = False
		self.moving_down = False
		
	def draw(self, surface):
		pygame.draw.rect(surface, self.color, self.bounds)
		
	def handle(self, key):
		if key == K_LEFT:
			self.moving_left = not self.moving_left
		elif key == K_RIGHT:
			self.moving_right = not self.moving_right
		elif key == K_UP:
			self.moving_up = not self.moving_up
		else: #K_DOWN
			self.moving_down = not self.moving_down
			
	def update(self):
		moving = False
		if self.moving_left:
			dx = -(min(self.speed, self.left))
			#dx = -(self.left)
			moving = True
		elif self.moving_right:
			dx = min(self.speed, c.screen_width - self.right) #
			moving = True
		if self.moving_up:
			#dy = -(self.top)
			dy = -(min(self.speed, self.top))
			moving = True
		elif self.moving_down:
			dy = min(self.speed, c.screen_height - self.bottom)
			moving = True
			
		if not moving:
			return
			
		if not 'dx' in vars():
			dx = 0
		if not 'dy' in vars():
			dy = 0
			
		self.move(dx, dy)