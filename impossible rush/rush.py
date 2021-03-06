import pygame
import random
from pygame.locals import *
class colorwheel(pygame.sprite.Sprite):
	"""docstring for colorwheel"""
	def __init__(self,x,y):
		self.top = "blue"
		self.x=x
		self.y=y
		self.image = pygame.image.load ("./images/colorwheel.png")
		self.redrect=pygame.Rect (200, 515, 105,35)

	def draw(self,screen):
		pygame.draw.rect(screen, (255,255,255),self.redrect,1)
		screen.blit (self.image,(self.x,self.y))
class ballred(pygame.sprite.Sprite):
	def __init__(self,x,y):
		self.color = "red"
		self.x=x
		self.y=y
		self.image = pygame.image.load ("./images/red circle.png")
		self.image = pygame.transform.scale(self.image, (35,35))
		self.rect=pygame.Rect (x, y, 35, 35)
	def draw(self,screen):
		screen.blit (self.image,(self.x,self.y))

class ballblue(pygame.sprite.Sprite):
	def __init__(self,x,y):
		self.color = "blue"
		self.x=x
		self.y=y
		self.image = pygame.image.load ("./images/bluecircle.png")
		self.image = pygame.transform.scale(self.image, (35,35))
		self.rect=pygame.Rect (x, y, 35, 35)
	def draw(self,screen):
		screen.blit (self.image,(self.x,self.y))


class ballyellow(pygame.sprite.Sprite):
	def __init__(self,x,y):
		self.color = "yellow"
		self.x=x
		self.y=y
		self.image = pygame.image.load ("./images/Yellow_circle.png")
		self.image = pygame.transform.scale(self.image, (35,35))
		self.rect=pygame.Rect (x, y, 35, 35)
	def draw(self,screen):
		screen.blit (self.image,(self.x,self.y))
class ballgreen(pygame.sprite.Sprite):
	def __init__(self,x,y):
		self.color = "green"
		self.x=x
		self.y=y
		self.image = pygame.image.load ("./images/green circle.jpg")
		self.image = pygame.transform.scale(self.image, (35,35))
		self.rect=pygame.Rect (x, y, 35, 35)
	def draw(self,screen):
		screen.blit (self.image,(self.x,self.y))

def chooseball():
	balllist=[ballyellow(215,-25),ballblue(215, -25),ballgreen(215, -25),ballred(215, -25)]
	return random.choice(balllist)
rotatecount=0
wheelcolor=["blue","green","yellow","red"]
pygame.init()
screen=pygame.display.set_mode ((500,750))
wheel=colorwheel(90,450)
ball1=chooseball()
clock=pygame.time.Clock()
font=pygame.font.Font(None,36)
text=font.render("Impossible Drop press,SPACE to continue",True,(0,0,0))
positiontitle=text.get_rect(centerx=250,centery=250)
title=True
while title:
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			title=False
		if event.type==KEYDOWN:
			if event.key==K_SPACE:
				title=False
	screen.fill((255,255,255))
	screen.blit(text,positiontitle)
	pygame.display.update()
	clock.tick(60)

running=True
while running:
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			running=False
		if event.type==KEYDOWN:
			if event.key==K_SPACE:
				rotatecount+=1
				wheel.top=wheelcolor[rotatecount%4]
				wheel.image=pygame.transform.rotate(wheel.image,90)
			if event.key==K_ESCAPE:
				pygame.quit()
				running=False
	screen.fill((255,255,255))
	ball1.y+=(5)
	rect = pygame.Rect(ball1.x, ball1.y, 35, 35)
	if wheel.redrect.colliderect(rect):
		if ball1.color==wheel.top:
			ball1=chooseball()
		else:
			pygame.quit()
			running=False

	#ball1.rect.move_ip(ball1.x, ball1.y)
	wheel.draw (screen)
	ball1.draw(screen)
	pygame.display.update()
	clock.tick(60)
