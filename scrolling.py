#
# Scrolling Demo
# Devs: Chelsea, Philip
#

import time
import random
from graphics import *

# The size of the level (in tiles)
LEVEL_WIDTH = 50
LEVEL_HEIGHT = 50

# The size of the viewport (in tiles)
VIEWPORT_WIDTH = 21
VIEWPORT_HEIGHT = 21

# The size of the window (in pixels)
TILE_SIZE = 24
WINDOW_WIDTH = TILE_SIZE * VIEWPORT_WIDTH
WINDOW_HEIGHT = TILE_SIZE * VIEWPORT_HEIGHT

def screen_pos (x,y):
    return (x*TILE_SIZE+10,y*TILE_SIZE+10)

def screen_pos_index (index):
    x = index % VIEWPORT_WIDTH
    y = (index - x) / VIEWPORT_WIDTH
    return screen_pos(x,y)

def index (x,y):
    return x + (y*LEVEL_WIDTH)

# The representation of data in the level array
# 0 empty   (player can be on this)
# 1 grass   (player can be on this)
# 2 tree    (player cannot be on this)
# 3 rat     (player cannot be this)

def create_random_level ():
    level = [0] * 2500
    for i in range(100):
        level[random.randint(0,2499)] = 1
    for i in range(50):
        level[random.randint(0,2499)] = 2
    return level

# def read_level (num):
#     screen = open('Levels/level' + str(num) + '.txt')
#     lines = []
#     for line in screen:
#         for ch in line:
#             if ch != '\n':
#                 ch = int(ch)
#                 lines.append(ch)
#     return lines

def create_screen (level,window,x,y):
    screen = []
    grass = 'grass.gif'
    tree = 'tree.gif'
    rat = 'rat.gif'

    def image (sx,sy,what):
        return Image(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2),what)

    # screen.append(level[index(x,y)])

    # for i in range(0,10):
    #     for j in range(0,10):
    #         screen.append(level[index(x+j,y+i)])
    #         screen.insert(0,level[index(x-j,y-i)])

    for i in range(y-10,y+11):
        for j in range(x-10,x+11):
            screen.append(level[index(j,i)])

    for (ind,cell) in enumerate(screen):
        if cell != 0:
            (sx,sy) = screen_pos_index(ind)
            if cell == 1:
                elt = image(sx,sy,grass)
            elif cell == 2:
                elt = image(sx,sy,tree)
            elif cell == 3:
                elt = image(sx,sy,rat)
            elt.draw(window)
    
# Player is created by Player(x,y,window,level,scr)
#   where (x,y) is the initial position of the player
#   in the level, window is the window created by
#   GraphWin, level is the level array, and scr
#   is a data structure that holds whatever interesting elements
#   you've displayed on the screen in create_screen(), presumably.

class Player (object):
    def __init__ (self,x,y,window,level,scr):
        (sx,sy) = screen_pos(x,y)
        self._pic = 't_android.gif'
        # self._img = Image(Point(sx+TILE_SIZE/2,sy+TILE_SIZE/2+2),self._pic)
        self._img = Image(Point(x+TILE_SIZE/2,y+TILE_SIZE/2+2),self._pic)
        self._window = window
        self._img.draw(window)
        self._level = level
        self._screen = scr
        self._x = x
        self._y = y

    def move (self,dx,dy):
        # MOVE THE PLAYER BY (dx,dy)
        # calculate new position:
        tx = self._x + dx
        ty = self._y + dy
        if tx >= 0 and ty >= 0 and tx < LEVEL_WIDTH and ty < LEVEL_HEIGHT:
            if self._level[index(tx,ty)] == 0:
                self._x = tx
                self._y = ty
                self._img.move(dx*TILE_SIZE,dy*TILE_SIZE)
        # make sure you call this when there is movement so that the
        # window can refresh
        self._window.update()

# The event queue
# There should be no need to change this

class EventQueue (object):
    def __init__ (self):
        self._contents = []

    # list kept ordered by time left before firing
    def enqueue (self,when,obj):
        for (i,entry) in enumerate(self._contents):
            if when < entry[0]:
                self._contents.insert(i,[when,obj])
                break
        else:
            self._contents.append([when,obj])

    def ready (self):
        if self._contents:
            return (self._contents[0][0]==0)
        else:
            return False
        
    def dequeue_if_ready (self):
        acted = self.ready()
        while self.ready():
            entry = self._contents.pop(0)
            entry[1].event(self)
        for entry in self._contents:
            entry[0] -= 1

# A simple class to register a "checking input from the player" event

MOVE = {
    'Left': (-1,0),
    'a' : (-1,0),
    'Right': (1,0),
    'd' : (1,0),
    'Up' : (0,-1),
    'w' : (0,-1),
    'Down' : (0,1),
    's' : (0,1)
}

class CheckInput (object):
    def __init__ (self,window,player):
        self._player = player
        self._window = window

    def event (self,q):
        # Note that checkKey() -- as does checkMouse()
        # automatially updates the window
        key = self._window.checkKey()
        if key == 'q':
            self._window.close()
            exit(0)
        if key in MOVE:
            (dx,dy) = MOVE[key]
            self._player.move(dx,dy)
        q.enqueue(1,self)

def main ():
    window = GraphWin("Scrolling Demo", 
                      WINDOW_WIDTH, WINDOW_HEIGHT,
                      autoflush=False)

    # num = raw_input('Which level? ')

    # level = read_level(num)
    level = create_random_level()

    # initial "center" of the screen is (25,25) in the level array
    scr = create_screen(level,window,25,25)

    # player starts at (25,25) as well...
    p = Player(25,25,window,level,scr)

    q = EventQueue()

    q.enqueue(1,CheckInput(window,p))

    while True:
        q.dequeue_if_ready()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
