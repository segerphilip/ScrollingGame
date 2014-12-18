from thing import *

class Character (Thing):
    def __init__ (self,name,desc):
        Thing.__init__(self,name,desc)
        rect = Rectangle(Point(1,1),
                         Point(TILE_SIZE-1,TILE_SIZE-1))
        rect.setFill("red")
        rect.setOutline("red")
        self._sprite = rect


    def move (self,dx,dy):
        tx = self._x + dx
        ty = self._y + dy
        if tx > 1 and ty > 1 and tx < LEVEL_WIDTH and ty < LEVEL_HEIGHT:
            if self._screen.tile(tx,ty) != 2 and self._screen.tile(tx,ty) != 1:
                for thing in self._screen._things:
                    if thing._x == tx and thing._y == ty and not thing.is_walkable():
                        return
                self._x = tx
                self._y = ty
                self._sprite.move(dx*TILE_SIZE,dy*TILE_SIZE)
        self._screen._window.update()

    def is_character (self):
        return True

    def is_thing (self):
        return False

    def is_walkable (self):
        return False

    def is_principal (self):
        return False