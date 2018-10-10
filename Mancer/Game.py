import pygame
import sys
import logging

class Game:
	def __init__(self, width, height):
		self.gameObjects = []
		
	def update(self):
		for o in self.gameObjects:
			o.update()
