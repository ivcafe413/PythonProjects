import pygame
import sys
import logging

from CollisionDetection.QuadTree import QuadTree

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
			for c in collidables:
				if o.bounds.colliderect(c.bounds):
					# Collision detected
					pass