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
			if not self==entity:
				if self.rect.colliderect(entity.rect):
					if self.speed_y<=0:
						self.rect.top=entity.rect.top+entity.rect.height
						self.position=(self.position[0],self.rect.top)
						self.speed_y=0
					else:
						self.rect.top=entity.rect.top-self.rect.height
						self.speed_y=0
						self.position=(self.position[0],self.rect.top)
						self.remaining_jumps=2
		self.rect.left=self.position[0]
		for entity in entities:
			if not self==entity:
				if self.rect.colliderect(entity.rect):
					if self.speed_x<=0:
						self.rect.left=entity.rect.left+entity.rect.width
						self.position=(self.rect.left, self.position[1])
						self.speed_x=0
					else:
						self.rect.left=entity.rect.left-self.rect.width
						self.speed_x=0
						self.position=(self.rect.left, self.position[1])



class platform(entity):
	def __init__(self,position):
		entity.__init__(self, globals.platform,position)
		



class player(entity):
	def __init__(self,position):
		entity.__init__(self, globals.character,position)
		self.remaining_jumps=3
		
	def should_move(self):
		return True

class bottom(platform):
	def __init__(self):
		entity.__init__(self, globals.bottom,(0,800))

class bullet(entity):
	def __init__(self,position,speed):
		entity.__init__(self, globals.bullet,position)
		self.speed_x=speed[0]
		self.speed_y=speed[1]
	def should_move(self):
		return True
		


		