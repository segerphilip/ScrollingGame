import random

# Tile size of the level
LEVEL_WIDTH = 50
LEVEL_HEIGHT = 50

# Tile size of the viewport (through which you view the level)
VIEWPORT_WIDTH = 21
VIEWPORT_HEIGHT = 21 

# Pixel size of a tile (which gives you the size of the window)
TILE_SIZE = 24

# Pixel size of the viewport
WINDOW_WIDTH = TILE_SIZE * VIEWPORT_WIDTH
WINDOW_HEIGHT = TILE_SIZE * VIEWPORT_HEIGHT

# Pixel size of the panel on the right where you can display stuff
WINDOW_RIGHTPANEL = 200

def read_level (num):
    screen = open('Levels/level' + str(num) + '.txt')
    lines = []
    for line in screen:
        for ch in line:
            if ch != '\n':
                ch = int(ch)
                lines.append(ch)
    return lines

#
# This implements a random level right now. 
# You'll probably want to replace this with something that 
# implements a specific map -- perhaps of Olin?
#
class Level (object):
    def __init__ (self):
        size = LEVEL_WIDTH * LEVEL_HEIGHT
        map = read_level(0)
        self._map = map

    def _pos (self,x,y):
        return x + (y*LEVEL_WIDTH);

    # return the tile at a given tile position in the level
    def tile (self,x,y):
        return self._map[self._pos(x,y)]
