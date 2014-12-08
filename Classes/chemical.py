from mobile import *

class Chemical (Mobile):

	def __init__ (self,name,desc):
		Thing.__init__(self,name,desc)
		self._pic = 'Resources/chemical.gif'
		self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)

	def use (self):
		# TODO: Get high
		pass