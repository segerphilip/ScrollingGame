from thing import *
from drug import *

class ChemTable (Thing):
    def __init__ (self,chems):
        Thing.__init__(self,"Chemical Table","Mix it up!")
        self._pic = 'Resources/chemtable.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)
        self._chems = chems

    def use (self,player):
        for chem in self._chems:
        	if not player.have_thing(chem):
        		self.explosion(player)
        	player._screen.delete(chem)
        d = Drug('Coke','drugs are... bad?').materialize(player._screen,0,0)
        d.take(player)


    def explosion (self,player):
    	print 'You exploded!'
        pass