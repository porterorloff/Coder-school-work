import pygame
from pygame.locals import *
import events
class app:
	def __init__(self):
		self._running=True
		self.screen=None
		self.size=self.weight,self.height=1400,800
	def on_init(self):
		pygame.init()
		self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		self._running=True
		self.background=pygame.image.load("background.jpg")
		self.platform=pygame.image.load("platform.png")
		self.camera=pygame.image.load("securitycamera.png")
		self.cannon=pygame.image.load("cannon.png")
		self.character=pygame.image.load("character.jpg")
		self.cannon =pygame.transform.rotate(self.cannon,90)
		self.images=[(self.platform,(400,450)),(self.platform, (100,600)),(self.background, (0,0)),(self.camera,(800,120)),(self.cannon,(110,120))]
	def on_event(self,event):
		if event.type==pygame.QUIT:
			self._running=False
		if event.type == pygame.KEYDOWN:
			if event.key == K_SPACE:


	def on_loop(self):
		pass

	def on_render(self):
		self.screen.fill([255,255,255])
		for coordinate in self.platforms:
			self.screen.blit(self.platform,coordinate)
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