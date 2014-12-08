from thing import *

class BenchPress (Thing):
    def __init__ (self):
        Thing.__init__(self,"BenchPress","Get swoll")
        self._pic = 'Resources/benchpress.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)

    def use (self,player):
        pass