from thing import *
from drug import *

class ChemTable (Thing):
    def __init__ (self,chems):
        Thing.__init__(self,"Chemical Table","\nmix it up!")
        self._pic = 'Resources/chemtable.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)
        self._chems = chems

    def use (self,player):
        for chem in self._chems:
            if not player.have_thing(chem):
                # self.explosion(player)
                self.com('Hm, I seem to\nbe missing something')
                return
        for chem in self._chems:
            player._inventory.remove(chem)
            player._screen.delete(chem)
        player._confidence = player._confidence + 1
        player.update_confidence()
        d = Drug('Coke','drugs are...\nbad?').materialize(player._screen,0,0)
        d.take(player)


    def explosion (self,player):
# TODO: Cover player in tar
        return