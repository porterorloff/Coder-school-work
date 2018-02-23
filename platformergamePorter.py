from entity import *
import pygame
from pygame.locals import *
import events
import globals
class app:
	def __init__(self):
		self._running=True
		self.screen=None
		self.size=self.weight,self.height=1400,800
	def on_init(self):
		pygame.init()
		self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		self._running=True
		self.character= character((0,0))
		self.entities=[platform((400,450)),platform((100,600)),entity(globals.camera,(800,120)),entity(globals.cannon,(130,120)),self.character]
	def on_event(self,event):
		if event.type==pygame.QUIT:
			self._running=False
		if event.type == pygame.KEYDOWN:
			if event.key == K_SPACE:
				self.character.speed_y-=5
	def on_loop(self):
		for entity in self.entities:
			if entity.should_move():
				entity.position=(entity.position[0]+entity.speed_x,entity.position[1]+entity.speed_y)
				entity.speed_y+=1

	def on_render(self):
		self.screen.fill([255,255,255])
		self.screen.blit(globals.background,(0,0))
		for entity in self.entities:
			self.screen.blit(entity.image,entity.position)
		pygame.display.update()

	def on_cleanup(self):
		pygame.quit()


	def on_execute(self):
		if self.on_init()==False:
			self._running=False
		while self._running:
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
			self.on_render()
		self.on_cleanup()















theApp=app()
theApp.on_execute() 