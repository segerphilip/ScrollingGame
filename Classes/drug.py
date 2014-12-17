from mobile import *

class Drug (Mobile):

	def __init__ (self,name,desc):
		Thing.__init__(self,name,desc)
		self._pic = 'Resources/drugs.gif'
		self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)

	# def use (self):
	# 	# TODO: Get high
	# 	pass

	def is_drug(self):
		return True