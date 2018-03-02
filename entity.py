import globals
import pygame
class entity:
	def __init__(self,image,position):
		self.image=image 
		self.position=position
		self.speed_x=0
		self.speed_y=0
		self.rect=pygame.Rect(self.position[0],self.position[1],self.image.get_width(),self.image.get_height())
	def should_move(self):
		return False
	def move(self,entities):
		self.position=(self.position[0]+self.speed_x,self.position[1]+self.speed_y)
		self.rect.top=self.position[1]
		for entity in entities:
			if self.rect.colliderect(entity.rect):
				 if self.speed_y<=0:
				 	self.rect.top=entity.rect.top+entity.rect.height
				 	self.speed_y=0
				 else:
				 	self.rect.top=entity.rect.top-self.rect.height
				 	self.speed_y=0

		self.rect.left=self.position[0]
		

class platform(entity):
	def __init__(self,position):
		entity.__init__(self, globals.platform,position)
		

class player(entity):
	def __init__(self,position):
		entity.__init__(self, globals.character,position)
		
	def should_move(self):
		return True