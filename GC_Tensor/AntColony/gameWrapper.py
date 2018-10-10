import sys
import pygame
import logging
import tensorflow as tf

from game import Game
from ant import Ant

MAX_EPSILON = 1
MIN_EPSILON = 0.01
LAMBDA = 0.001
GAMMA = 0.99
BATCH_SIZE = 50

class GameWrapper:
	def __init__(self, sess, max_eps, min_eps, decay, render=True):
		self.render = render

		# Game Loop runner stuff
		self.paused = False
		self.targetRenderFps = 60
		self.targetUpdateFps = 60
		self.RENDER_MS_PF = (1 / self.targetRenderFps) * 1000
		self.UPDATE_MS_PF = (1 / self.targetUpdateFps) * 1000
		self.clock = pygame.time.Clock()
		self.elapsedTime = 0

		# Game environment initialization
		self.game = Game(10, 10)
		ant = Ant(300, 200, 20, 20, sess, max_eps, min_eps, decay, GAMMA, BATCH_SIZE)
		self.game.objects.append(ant)

	def run(self):
		pygame.init()

		while True:
			self.elapsedTime += self.clock.get_time()

			# Handle Events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			done = None
			while self.elapsedTime >= (self.UPDATE_MS_PF):
				done = self.game.update()
				if done:
					break

				self.elapsedTime -= (self.UPDATE_MS_PF)

			if done:
				break

			# Render
			if self.render:
				self.game.render()

			# Clock ticks for FPS and render FPS counter
			self.clockFrame()

	def clockFrame(self):
		fps = self.clock.get_fps()
		pygame.display.set_caption("FPS: {0:2f}".format(fps))
		self.clock.tick(self.targetRenderFps)
		
def main():
	logging.basicConfig(level=logging.INFO)

	with tf.Session() as sess:
		sess.run(tf.global_variables_initializer())
		game = GameWrapper(sess, MAX_EPSILON, MIN_EPSILON, LAMBDA)
		
		game.run()
	
if __name__ == '__main__':
	main()