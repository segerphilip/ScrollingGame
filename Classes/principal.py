from npc import *
import random

MOVES = [(1,0), (-1,0),
         (0,1), (0,-1),
         (0,0)]

NPC_DELAY = 30

class Principal (NPC):

    def __init__ (self,name,desc,player):
        NPC.__init__(self,name,desc,player)
        self._pic = 'Resources/principal.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)

    def prowl (self):
        # TODO: remove confidence when near player
        pass

    def move (self, dx, dy):
        tx = self._x + dx
        ty = self._y + dy
        if tx > 1 and ty > 1 and tx < LEVEL_WIDTH and ty < LEVEL_HEIGHT:
            if (tx < self._p._x+8 or tx > self._p._x+8) and (ty < self._p._y+8 or ty > self._p._y+8):
                if self._screen.tile(tx,ty) != 2 and self._screen.tile(tx,ty) != 1:
                    for thing in self._screen._things:
                        if thing._x == tx and thing._y == ty and not thing.is_walkable():
                            return
                    self._x = tx
                    self._y = ty
                    self._sprite.move(dx*TILE_SIZE,dy*TILE_SIZE)
        self._screen._window.update()