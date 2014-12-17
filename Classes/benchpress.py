from thing import *

class BenchPress (Thing):
    def __init__ (self):
        Thing.__init__(self,"BenchPress","Get swoll")
        self._pic = 'Resources/benchpress.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)
        self._skill = 1

    def use (self,player):
        for t in self._screen._things:
            if ((t._x == self._x + 2 or t._x == self._x - 2) and t._y == self._y) or ((t._y == self._y + 2 or t._y == self._y - 2) and t._x == self._x):
                if t.is_character():
                    player._confidence = player._confidence + 0.5*self._skill
                else:
                    self._skill += 1