from mobile import *

class Guitar (Mobile):

    def __init__ (self,name,desc):
        Thing.__init__(self,name,desc)
        self._pic = 'Resources/guitar.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)
        self._skill = 0

    def use (self):
        if self._skill < 5:
            self.learn()
        else:
            self.play()

    def play (self):
        print 'try play'
        for t in self._screen._things:
            print 'FIXIT'
            # if ((t._x == player._x + 1 or t._x == player._x - 1) and t._y == player._y) or ((t._y == player._y + 1 or t._y == player._y - 1) and t._x == player._x):
                # if t.is_character():
                    # player._confidence = player._confidence + 1
                    # print 'play'

    def learn (self):
        self._skill += 1
        print 'learn'
