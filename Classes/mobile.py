from thing import *

class Mobile (Thing):

    def __init__ (self,name,desc):
        Thing.__init__(self,name,desc)

    def take (self,player):
        if ( (self._x == player._x + 1 or self._x == player._x - 1) and self._y == player._y) or ((self._y == player._y + 1 or self._y == player._y - 1) and self._x == player._x):
            player._inventory.append(self)
            player._screen._window.delItem(self._sprite)
            self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)
            self._x = WINDOW_WIDTH + 10
            self._y = TILE_SIZE*i + 10
            player._screen.add(self,self._x,self._y)

    def drop (self,player):
        if self in player._inventory:
            player._inventory.remove(self)
            player._screen._window.delItem(self._sprite)
            self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)
            self._x = player._x + 1
            self._y = player._y
            player._screen.add(self,self._x,self._y)

    def is_mobile_thing (self):
        return True
