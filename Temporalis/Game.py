import pygame
import sys
import logging

from CollisionDetection.QuadTree import QuadTree
from Constants.UserEvents import *

class Game:
	def __init__(self, width, height):
		self.gameObjects = []
		self.quadTree = QuadTree(0, 0, width, height)
		
	def update(self):
		self.quadTree.clear()
		for o in self.gameObjects:
			o.update()
			self.quadTree.insert(o)
			
		for o in self.gameObjects:
			collidables = self.quadTree.getCollidableObjects(o)
			# For each collidable, Check for collision against o
			if collidables:
				for c in collidables:
					if o.bounds.colliderect(c.bounds):
						# Collision detected
						pygame.event.post(pygame.event.Event(COLLISION, game=self, obj1=o, obj2=c))
			self.quadTree.remove(o)

	def get(self, objType):
		"""Return all objects that are instance of type (returns generator)"""
		for o in self.gameObjects:
			if isinstance(o, objType):
				yield o