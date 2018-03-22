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
		self.character= player((0,0))
		self.minigun=minigun((130,120))
		self.entities=[platform((400,450)),platform((100,600)),entity(globals.camera,(800,120)),self.character,bottom(),self.minigun]
	def on_event(self,event):
		if event.type==pygame.QUIT:
			self._running=False
		if event.type == pygame.KEYDOWN:
			if event.key == K_SPACE:
				if self.character.remaining_jumps>0:
					self.character.remaining_jumps-=1			
					self.character.speed_y-=10
			if event.key == K_d:
				self.character.speed_x=10
			if event.key == K_a:
				self.character.speed_x=-10



		if event.type == pygame.KEYUP:
			if event.key == K_d:
				self.character.speed_x = 0
			if event.key==K_a:
				self.character.speed_x=0

	def on_loop(self):
		for entity in self.entities:
			if entity.should_move():
				entity.move(self.entities)
				entity.speed_y+=0.5
		self.minigun.loops_since_shot+=1
		if self.minigun.loops_since_shot>5:
			self.minigun.loops_since_shot=0
			bulletposition=(self.minigun.position[0],self.minigun.position[1]+300)
			self.entities.append(bullet(bulletposition,(0,20)))

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














clock = pygame.time.Clock()
clock.tick(60)
theApp=app()
theApp.on_execute() 