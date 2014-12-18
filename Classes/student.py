from npc import *
import random

MOVES = [(1,0), (-1,0),
         (0,1), (0,-1),
         (0,0)]

NPC_DELAY = 30

class Student (NPC):

    def __init__ (self,name,desc,player,img):
        NPC.__init__(self,name,desc,player)
        self._pic = img
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)
        self._direction = random.randrange(4)