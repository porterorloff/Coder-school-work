import pygame
from pygame.locals import *
pygame.init()
class Player:
	def __init__(self):
		self.image = pygame.image.load("skulltrooper.png")
		self.image=pygame.transform.scale(self.image,(200,200))
		self.x = 0
		self.y = 0 

	def shoot(self, direction):
		


	def draw(self):
		self.rect=screen.blit(self.image,(self.x, self.y))

class Bullet:
	
	def __init__(self, myimage, shooter):
		self.x=shooter.x
		self.y=shooter.y
		self.image=pygame.image.load(myimage)
		self.image=pygame.transform.scale(self.image,(20,10))
		self.bulletspeed=20


	def shoot(self, direction):
		self.rect=screen.blit(self.image,(self.x, self.y))
		if direction==0:
			self.y-=bulletspeed
		if direction==1:
			self.x+=bulletspeed
		if direction==2:
			self.y+=bulletspeed
		if direction==3:
			self.x-=bulletspeed

	def draw(self):
		self.rect=screen.blit(self.image,(self.x, self.y))

player=Player()

clock=pygame.time.Clock()
class Object:
	def __init__(self,x,y,image):
		self.image = pygame.image.load(image)
		self.image=pygame.transform.scale(self.image,(200,200))
		self.x = x
		self.y = y 

	def draw(self):
		self.rect=screen.blit(self.image,(self.x, self.y))



		
done = False

bush = Object(500,300, "bush.jpg")
screen = pygame.display.set_mode((1400, 1080))

while not done:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done = True

	if pygame.key.get_pressed()[K_w]:
	   player.y -=5  


	if pygame.key.get_pressed()[K_s]:
	   player.y +=5  


	if pygame.key.get_pressed()[K_a]:
	   player.x -=5  


	if pygame.key.get_pressed()[K_d]:
	   player.x +=5  



	if pygame.key.get_pressed()[K_UP]:
	   bush.y -=5  


	if pygame.key.get_pressed()[K_DOWN]:
	   bush.y +=5  


	if pygame.key.get_pressed()[K_LEFT]:
	   bush.x -=5  


	if pygame.key.get_pressed()[K_RIGHT]:
	   bush.x +=5  

	if pygame.key.get_pressed()[K_u]:


	if pygame.key.get_pressed()[K_j]:


	if pygame.key.get_pressed()[K_k]:


	if pygame.key.get_pressed()[K_h]:


	if pygame.key.get_pressed()[K_KP8]:


	if pygame.key.get_pressed()[K_KP5]:


	if pygame.key.get_pressed()[K_KP6]:


	if pygame.key.get_pressed()[K_KP4]:

		

	screen.fill((255,255,255))


	player.draw()
	bush.draw()
	pygame.display.update()




	clock.tick(40)
















































	"""juLIAN YOU HAVE 3 WINS YOU ARE NOT GOOD i LOOKED UP YOUR REAL STATS i AM A HACKER PORTER COMING IN WITH THE WEED BUCKS JULIAN
				COMING IN WITH THE NASTY PANTS HE SMELLS LIKE A BIG FART DONT GET NEAR HIM PORTER COMING IN WITH THE WEED BUCKS SMOKE SMOKE
				i YU S STPD THE FIRST 3 DOUS WE PLAYED YOU GOT 2 KILLS I GOT 5 U ARE A TRASH CAN GO CATCHA FART BECAUSE THERE IS A BAD FART 
				AHEAD NAMED JULIAN"""