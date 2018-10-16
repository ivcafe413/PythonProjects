import pygame
import sys
import logging

from CollisionDetection import QuadTree.*

class Game:
	def __init__(self, width, height):
		self.gameObjects = []
		self.quadTree = QuadTree(0, 0, width, height)
		
	def update(self):
		quadTree.clear()
		for o in self.gameObjects:
			o.update()
			quadTree.insert(o)
			
		for o in self.gameObjects:
			collidables = quadTree.getCollidableObjects(o)
			# TODO: For each collidable, Check for collision against o