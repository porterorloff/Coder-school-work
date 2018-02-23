import globals
class entity:
	def __init__(self,image,position):
		self.image=image 
		self.position=position
		self.speed_x=0
		self.speed_y=0
		self.rect=pygame.Rect(self.position[0],self.position[1],self.image.get_width(),self.image.get_height())
	def should_move(self):
		return False
	def move(self):
		self.position=(self.position[0]+self.speed_x,self.position[1]+self.speed_y)
		

class platform(entity):
	def __init__(self,position):
		super(platform,self).__init__(globals.platform,position)
		

class character(entity):
	def __init__(self,position):
		super(character,self).__init__(globals.character,position)
		
	def should_move(self):
		return True