from thing import *

class Mobile (Thing):

    def __init__ (self,name,desc):
        Thing.__init__(self,name,desc)

    def take (self,player):
        player._inventory.append(self)

    def drop (self,player):
        if self in player._inventory:
            player._inventory.remove(self)

    def is_mobile_thing (self):
        return True
