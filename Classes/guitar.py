from mobile import *
import time

class Guitar (Mobile):

    def __init__ (self,name,desc):
        Thing.__init__(self,name,desc)
        self._pic = 'Resources/guitar.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)
        self._skill = 0

    def use (self,player):
        if self._skill < 5:
            self.learn()
        else:
            self.play(player)

    def play (self,player):
        for t in self._screen._things:
            if ((t._x == player._x + 1 or t._x == player._x - 1) and t._y == player._y) or ((t._y == player._y + 1 or t._y == player._y - 1) and t._x == player._x):
                if t.is_character():
                    if t.is_principal():
                        t._anger = t._anger + 1
                        t.update_anger()
                        t.com('Stop goofing off!')
                        player._confidence = player._confidence + 0.5
                        player.update_confidence()
                    else:
                        player._confidence = player._confidence + 0.5
                        player.update_confidence()

    def learn (self):
        self._skill += 1
        if self._skill < 5:
            self.com('Practicing,\nplease wait.')
            time.sleep(1)
            self.com('You leared some! You\nnow know ' + str(self._skill) + ' out of 5.')
        else:
            self.com('You know how\nto play guitar!')
