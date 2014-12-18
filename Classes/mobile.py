from thing import *

class Mobile (Thing):

    def __init__ (self,name,desc):
        Thing.__init__(self,name,desc)

    def take (self,player):
        player._inventory.append(self)
        self._screen._things.remove(self)

        # fg = Rectangle(Point(WINDOW_WIDTH+TILE_SIZE,TILE_SIZE*(1+1.5*len(player._inventory))),
        #                    Point(WINDOW_WIDTH+2*TILE_SIZE,TILE_SIZE*(1+1.5*len(player._inventory)) + TILE_SIZE))
        # fg.setFill("black")
        # fg.draw(self._screen._window)
        self.sprite().move(((VIEWPORT_WIDTH+1)-(self._x-(self._screen._cx-(VIEWPORT_WIDTH-1)/2)))*TILE_SIZE,
                           ((1+1.5*len(player._inventory)-(self._y-(self._screen._cy-(VIEWPORT_HEIGHT-1)/2)))*TILE_SIZE))
        m = self.name() + ': ' + self.description()
        self.com(m)

    def use (self,player):
        self._screen.delete(self)

    def is_mobile_thing (self):
        return True

    def is_drug (self):
        return False
