from mobile import *

class Guitar (Mobile):

	def __init__ (self,name,desc):
		Thing.__init__(self,name,desc)
		self._pic = 'Resources/guitar.gif'
		self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)

	def play (self):
		pass

	def learn (self):
		pass
