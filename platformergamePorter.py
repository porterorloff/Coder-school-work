import pygame
from pygame.locals import *
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
		self.cannon =pygame.transform.rotate(self.cannon,90)
	def on_event(self,event):
		if event.type==pygame.QUIT:
			self._running=False
	def on_loop(self):
		pass

	def on_render(self):
		self.screen.fill([255,255,255])
		self.screen.blit(self.background,(0,0))
		self.screen.blit(self.platform,(100,600))
		self.screen.blit(self.platform,(100,600))
		self.screen.blit(self.platform,(400,400))
		self.screen.blit(self.camera,(800,120))
		self.screen.blit(self.cannon,(800,120))

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