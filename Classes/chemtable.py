from thing import *

#
# Example of a kind of thing with its specific sprite
# (here, a rather boring gray rectangle.)
#
class ChemTable (Thing):
    def __init__ (self):
        Thing.__init__(self,"Olin statue","A statue of F. W. Olin")
        self._pic = 'Resources/statue.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)