import pygame
from pygame.locals import *
screenwidth = 1400
screenheight = 700
ballwidth=100
ballheight=100
paddle_image=pygame.image.load("./images/blah.png")
paddle_image=pygame.transform.scale(paddle_image,(500,450))
ball_image=pygame.image.load("./images/ball.png")
ball_image=pygame.transform.scale(ball_image,(ballwidth,ballheight))
class ball(pygame.sprite.Sprite):
	def __init__(self):
		self.x=700
		self.y=200
		self.rect=pygame.Rect(self.x,self.y,100,100)
		self.image=ball_image
	def draw(self,screen):
		screen.blit(self.image,[self.x,self.y])

				
class paddle(pygame.sprite.Sprite):
	def __init__(self):
		self.x=700
		self.y=400
		self.image=paddle_image
		self.rect=pygame.Rect(self.x,self.y,500,450)
	def draw(self,screen):
		screen.blit(self.image,[self.x,self.y])
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((screenwidth,screenheight))
paddle1 = paddle()

ball1=ball()
done=False
pygame.key.set_repeat(1,5)
balldirecty=5
balldirectx=5
while not done:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True	
		if event.type==pygame.KEYDOWN:
			if event.key == K_RIGHT:
				paddle1.x+=10
			if event.key == K_LEFT:
				paddle1.x+=-10
	if ball1.x > screenwidth-ballwidth:
		balldirectx=-1*balldirectx
	if ball1.x <= 0:
		balldirectx=-1*balldirectx
	if ball1.y > screenheight-ballheight:
		balldirecty=-1*balldirecty
	if ball1.y <= 0:
		balldirecty=-1*balldirecty
	ball1.x = ball1.x + balldirectx
	ball1.y = ball1.y + balldirecty
	screen.fill((255,255,255))
	paddle1.draw(screen)
	ball1.draw(screen)
	pygame.display.update()
	clock.tick(60)
pygame.quit()