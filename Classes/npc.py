from character import *
import random

MOVES = [(1,0), (-1,0),
         (0,1), (0,-1),
         (0,0)]

NPC_DELAY = 30

class NPC (Character):
    def __init__ (self,name,desc):
        Character.__init__(self,name,desc)
        log("NPC.__init__ for "+str(self))
        self._pic = 'Resources/NPC.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)
        self._direction = random.randrange(4)

    def register (self,q,freq):
        self._freq = freq
        q.enqueue(freq,self)
        return self

    def event (self,q):
        # log("event for "+str(self))
        x,y = random.choice(MOVES)
        self.move(x,y)
        q.enqueue(NPC_DELAY,self)

    def talk (self,player):
        log("Hello from" + str(self))
