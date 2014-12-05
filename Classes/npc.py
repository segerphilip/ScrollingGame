from character import *
import random

MOVES = [(1,0), (-1,0),
         (0,1), (0,-1),
         (0,0)]

RAT_DELAY = 10

# 
# A Rat is an example of a character which defines an event that makes
# the rat move, so that it can be queued into the event queue to enable
# that behavior. (Which is right now unfortunately not implemented.)
#
class NPC (Character):
    def __init__ (self,name,desc):
        Character.__init__(self,name,desc)
        log("Rat.__init__ for "+str(self))
        self._pic = 'rat.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)
        self._direction = random.randrange(4)

    # A helper method to register the Rat with the event queue
    # Call this method with a queue and a time delay before
    # the event is called
    # Note that the method returns the object itself, so we can
    # use method chaining, which is cool (though not as cool as
    # bowties...)

    def register (self,q,freq):
        self._freq = freq
        q.enqueue(freq,self)
        return self

    # this gets called from event queue when the time is right

    def event (self,q):
        log("event for "+str(self))
        x,y = random.choice(MOVES)
        self.move(x,y)
        q.enqueue(RAT_DELAY,self)
