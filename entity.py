import globals
class entity:
	def __init__(self,image,position):
		self.image=image 
		self.position=position


class platform(entity):
	def __init__(self,position):
		self.image=globals.platform 
		self.position=position


class character(entity):
	def __init__(self,position):
		self.image=globals.character
		self.position=position
		self.speed_y=0
		self.speed_x=0
		