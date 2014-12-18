from mobile import *
import time

class Guitar (Mobile):

    def __init__ (self,name,desc):
        Thing.__init__(self,name,desc)
        self._pic = 'Resources/guitar.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)
        self._skill = 0

    def use (self,player):
        if self._skill < 10:
            self.learn()
        else:
            self.play(player)

    def play (self,player):
        for t in self._screen._things:
            if ((t._x == player._x + 1 or t._x == player._x - 1) and t._y == player._y) or ((t._y == player._y + 1 or t._y == player._y - 1) and t._x == player._x):
                if t.is_character():
                    player._confidence = player._confidence + 1
                    player.update_confidence()

    def learn (self):
        self._skill += 1
        if self._skill < 10:
            time.sleep(2)
            self.com('You leared some! You\nnow know ' + str(self._skill) + ' out of 10.')
        else:
            self.com('You know how\nto play guitar!')
