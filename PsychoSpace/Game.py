import pygame
import sys
import logging

import Config as c
from collections import defaultdict

class GameState:
	def __init__(self):
		#Game State
		self.objects = []
		self.paused = False
		self.targetRenderFps = 60
		self.targetUpdateFps = 60
		self.RENDER_MS_PF = (1 / self.targetRenderFps) * 1000
		self.UPDATE_MS_PF = (1 / self.targetUpdateFps) * 1000

class Game:
	def __init__(self, width, height):
		pygame.init()
		self.state = GameState()
		
		self.surface = pygame.display.set_mode((width, height))
		self.clock = pygame.time.Clock()		
		
		self.elapsedTime = 0
		self.event_handlers = defaultdict(list)
		self.keydown_handlers = defaultdict(list)
		self.keyup_handlers = defaultdict(list)
		
	#Todo: At some point, migrate key handling into state, to pass state into same handler function signature for all handlers, able to handle in contained code
	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				for handler in self.keydown_handlers[event.key]:
					handler(event.key)
			elif event.type == pygame.KEYUP:
				for handler in self.keyup_handlers[event.key]:
					handler(event.key)
			else:
				#self.event_handlers[event.type]()
				for handler in self.event_handlers[event.type]:
					handler(self.state)
				
	def update(self, state):
		for o in self.state.objects:
			o.update(state)
				
	def draw(self):
		for o in self.state.objects:
			o.draw(self.surface)
		
	def run(self):
		while True:
			self.elapsedTime += self.clock.get_time()
			# if self.elapsedTime >= (self.RENDER_MS_PF):
			
			self.handle_events()
			
			#possibility of variable update time frame to 'learn' and balance update speed real-time
			if not self.state.paused:
				while self.elapsedTime >= self.state.UPDATE_MS_PF:
					if(self.elapsedTime >= (self.state.UPDATE_MS_PF * 2)):
						logging.warning("Lag Frame: {0:n} over {1:n}".format(self.elapsedTime - self.state.RENDER_MS_PF, self.state.RENDER_MS_PF))
					self.update(self.state) #TODO: Passing in update MS?
					self.elapsedTime -= self.state.UPDATE_MS_PF
			
			self.render() #TODO: passing in leftover elapsed time over Render MS for % for render extrapolation
			self.clockFrame()
			
	def render(self):
		self.surface.fill(c.burlywood)
		self.draw()
		pygame.display.update()
		
	def clockFrame(self):
		fps = self.clock.get_fps()
		pygame.display.set_caption("FPS: {0:2f}".format(fps))
		self.clock.tick(self.state.targetRenderFps)