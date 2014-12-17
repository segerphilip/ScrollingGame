from npc import *
import random

MOVES = [(1,0), (-1,0),
         (0,1), (0,-1),
         (0,0)]

NPC_DELAY = 30

class Principal (NPC):

    def __init__ (self,name,desc,player):
        NPC.__init__(self,name,desc,player)
        log("Principal.__init__ for "+str(self))
        self._pic = 'Resources/principal.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)
        self._direction = random.randrange(4)

    def prowl (self):
        # TODO: Search for bad students
        # New pathfinding to patrol the halls during certain time intervals
        pass