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
        self._pic = 'Resources/girl.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)
        self._direction = random.randrange(4)

    def compare (self,player):
        # TODO: judge player confidence level
        pass

    def strut (self):
        # TODO: More interesting things
        pass

    def talk (self,player):
        for thing in player._inventory:
            if thing.is_drug():
                print "I'll take that coke! Thanks!"
                player._confidence = player._confidence + 2
                player.update_confidence()
                thing.use(player)
                player._inventory.remove(thing)
                return
        if player._confidence <5:
            print "I don't talk to losers"
        elif player._confidence >= 5 and player._confidence < 10:
            print "You're alright I guess"
        else:
            print "Of course I'll go to prom with you!"
            player._screen.win()