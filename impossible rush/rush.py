import pygame
from pygame.locals import *
class colorwheel(pygame.sprite.Sprite):
	"""docstring for colorwheel"""
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.image = pygame.image.load ("./images/colorwheel.png")
	def draw(self,screen):
		screen.blit (self.image,(self.x,self.y))
pygame.init()
screen=pygame.display.set_mode ((500,750))
wheel=colorwheel(90,350)
clock=pygame.time.Clock()
running=True
while running:
	for event in pygame.event.get():
		if event.type==KEYDOWN:
			if event.key==K_SPACE:
				wheel.image=pygame.transform.rotate(wheel.image,90)
			if event.key==K_ESCAPE:
				pygame.quit()
				running=False
	screen.fill((255,255,255))	
	wheel.draw (screen)
	pygame.display.update()
	clock.tick(40)


