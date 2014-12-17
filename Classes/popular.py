from npc import *
import random

MOVES = [(1,0), (-1,0),
         (0,1), (0,-1),
         (0,0)]

NPC_DELAY = 30

class Popular (NPC):

    def __init__ (self,name,desc,player):
        NPC.__init__(self,name,desc,player)
        log("Popular.__init__ for "+str(self))
        self._pic = 'Resources/girl.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)
        self._direction = random.randrange(4)

    def compare (self,player):
        # TODO: judge player confidence level
        pass

    def strut (self):
        # TODO: More interesting things
        pass

    def talk (self):
        for thing in self._p._inventory:
            if thing.is_drug():
                self.com("I'll take that coke! Thanks!")
                self._p._confidence = self._p._confidence + 2
                self._p.update_confidence()
                thing.use(self._p)
                self._p._inventory.remove(thing)
                return
        if self._p._confidence <5:
            self.com("I don't talk to losers")
        elif self._p._confidence >= 5 and self._p._confidence < 10:
            self.com("You're alright I guess")
        else:
            self.com("Of course I'll go to prom with you!")
            self._p._screen.win()