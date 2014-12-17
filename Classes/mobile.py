from thing import *

class Mobile (Thing):

    def __init__ (self,name,desc):
        Thing.__init__(self,name,desc)

    def take (self,player):
        fg = Rectangle(Point(WINDOW_WIDTH+5,100),
                   Point(WINDOW_WIDTH+195,125))
        fg.setFill("grey")
        fg.setOutline("black")
        fg.draw(self._screen._window)


        player._inventory.append(self)
        self._screen._things.remove(self)
        # self._sprite.move(LEVEL_WIDTH-(self._x*TILE_SIZE),LEVEL_HEIGHT-(self._y*TILE_SIZE))
        self._x = VIEWPORT_WIDTH+15
        self._y = len(player._inventory) + 15

    def use (self,player):
        self._screen.delete(self)

    def is_mobile_thing (self):
        return True

    def is_drug (self):
        return False
