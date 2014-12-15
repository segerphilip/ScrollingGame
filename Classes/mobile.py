from thing import *

class Mobile (Thing):

    def __init__ (self,name,desc):
        Thing.__init__(self,name,desc)

    def take (self,player):
        player._inventory.append(self)
        self._screen._things.remove(self)
        self._sprite.move((-self._x+VIEWPORT_WIDTH+15)*TILE_SIZE,(-self._y + len(player._inventory) + 15)*TILE_SIZE)
        self._x = VIEWPORT_WIDTH+15
        self._y = len(player._inventory) + 15

    def use (self,player):
        self._screen.delete(self)

    # def drop (self,player):
    #     if self in player._inventory:
    #         player._inventory.remove(self)
    #         player._screen._window.delItem(self._sprite)
    #         self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)
    #         self._x = player._x + 1
    #         self._y = player._y
    #         player._screen.add(self,self._x,self._y)

    def is_mobile_thing (self):
        return True
