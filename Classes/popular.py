from npc import *
import random

MOVES = [(1,0), (-1,0),
         (0,1), (0,-1),
         (0,0)]

NPC_DELAY = 30

class Popular (NPC):

    def __init__ (self,name,desc):
        NPC.__init__(self,name,desc)
        log("Popular.__init__ for "+str(self))
        self._pic = 'Resources/popular.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)
        self._direction = random.randrange(4)

    def compare (self,player):
        # TODO: judge player confidence level
        pass

    def strut (self):
        # TODO: More interesting things
        pass