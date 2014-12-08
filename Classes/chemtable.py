from thing import *

class ChemTable (Thing):
    def __init__ (self):
        Thing.__init__(self,"Chemical Table","Mix it up!")
        self._pic = 'Resources/chemtable.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)

    def use (self,player):
        pass

    def explosion (self,player):
        pass