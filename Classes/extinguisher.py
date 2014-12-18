from mobile import *

class Extinguisher (Mobile):

    def __init__ (self,name,desc):
        Thing.__init__(self,name,desc)
        self._pic = 'Resources/firext.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)

    def use (self,player):
        for t in self._screen._things:
            if ((t._x == player._x + 1 or t._x == player._x - 1) and t._y == player._y) or ((t._y == player._y + 1 or t._y == player._y - 1) and t._x == player._x):
                if t.is_character():
                    if t.is_principal:
                        t._anger = t._anger + 1
                        t.com('How dare you!')
                        player._confidence = player._confidence + 0.5
                        player.update_confidence()
                    else:
                        t.com("Don't spray me! \n Spray Mr. Pucella!")