from mobile import *

class Guitar (Mobile):

    def __init__ (self,name,desc):
        Thing.__init__(self,name,desc)
        self._pic = 'Resources/guitar.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)
        self._skill = 0

    def use (self):
        if self._skill < 5:
            learn()
        else:
            play()

    def play (self):
        print 'try play'
        for t in self._screen._things:
            if ((t._x == self._x + 1 or t._x == self._x - 1) and t._y == self._y) or ((t._y == self._y + 1 or t._y == self._y - 1) and t._x == self._x):
                if t.is_character():
                    player._confidence = player._confidence + 1
                    print 'play'

    def learn (self):
        self._skill += 1
        print 'learn'
