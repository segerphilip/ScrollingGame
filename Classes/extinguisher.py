from mobile import *

class Extinguisher (Mobile):

	def __init__ (self,name,desc):
		Thing.__init__(self,name,desc)
		self._pic = 'Resources/chemical.gif'
		self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)

	def use (self):
		pass