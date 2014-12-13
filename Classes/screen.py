from graphics import *
from thing import *

# Tile size of the level
LEVEL_WIDTH = 50
LEVEL_HEIGHT = 50

# Tile size of the viewport (through which you view the level)
VIEWPORT_WIDTH = 21
VIEWPORT_HEIGHT = 21

# Pixel size of a tile (which gives you the size of the window)
TILE_SIZE = 50

# Pixel size of the viewport
WINDOW_WIDTH = TILE_SIZE * VIEWPORT_WIDTH
WINDOW_HEIGHT = TILE_SIZE * VIEWPORT_HEIGHT

# Pixel size of the panel on the right where you can display stuff
WINDOW_RIGHTPANEL = 200


# 
# 0 - floor
# 1 - wall
# 2 - lockers
# 3 - door
# 4 - stairs
#
# A Screen is a representation of the level displayed in the 
# viewport, with a representation for all the tiles and a 
# representation for the objects in the world currently 
# visible. Managing all of that is key. 
#
# For simplicity, a Screen object contain a reference to the
# level it is displaying, and also to the window in which it
# draws its elements. So you can use the Screen object to 
# mediate access to both the level and the window if you need
# to access them.
# 
# You'll DEFINITELY want to add methods to this class. 
# Like, a lot of them.
#
class Screen (object):
    def __init__ (self,level,window,cx,cy):
        self._level = level
        self._window = window
        self._cx = cx    # the initial center tile position 
        self._cy = cy    #  of the screen
        self._things = []
        # Background is black
        bg = Rectangle(Point(-20,-20),Point(WINDOW_WIDTH+20,WINDOW_HEIGHT+20))
        bg.setFill("black")
        bg.setOutline("black")
        bg.draw(window)
        # here, you want to draw the tiles that are visible
        # and possible record them for future manipulation
        # you'll probably want to change this at some point to
        # get scrolling to work right...
        dx = (VIEWPORT_WIDTH-1)/2
        dy = (VIEWPORT_HEIGHT-1)/2
        self._corner = (self._cx-dx,self._cy-dy)
        for y in range(cy-dy,cy+dy+1):
            for x in range(cx-dx,cx+dx+1):
                sx = (x-(cx-dx) +1) * TILE_SIZE
                sy = (y-(cy-dy) +1) * TILE_SIZE
                elt = Rectangle(Point(sx,sy),
                                Point(sx+TILE_SIZE,sy+TILE_SIZE))
                if self.tile(x,y) == 0:
                    elt = Image(Point(sx,sy),'Resources/tiles.gif')
                if self.tile(x,y) == 1:
                    elt = Image(Point(sx,sy),'Resources/wall.gif')
                if self.tile(x,y) == 2:
                    elt = Image(Point(sx,sy),'Resources/lockers.gif')
                if self.tile(x,y) == 3:
                    elt = Image(Point(sx,sy),'Resources/door.gif')
                if self.tile(x,y) == 4:
                    elt = Image(Point(sx,sy),'Resources/stairs.gif')
                elt.draw(window)

    # return the tile at a given tile position
    def tile (self,x,y):
        return self._level.tile(x,y)

    # add a thing to the screen at a given position
    def add (self,item,x,y):
        # first, move object into given position
        item.sprite().move((x-(self._cx-(VIEWPORT_WIDTH-1)/2))*TILE_SIZE,
                           (y-(self._cy-(VIEWPORT_HEIGHT-1)/2))*TILE_SIZE)
        item.sprite().draw(self._window)
        # WRITE ME!   You'll have to figure out how to manage these
        # because chances are when you scroll these will not move!


    # helper method to get at underlying window
    def window (self):
        return self._window

    def scroll (self,px,py):
        self._cx = self._cx + px
        self._cy = self._cy + py
        dx = (VIEWPORT_WIDTH-1)/2
        dy = (VIEWPORT_HEIGHT-1)/2
        self._corner = (self._cx-dx,self._cy-dy)
        for y in range(self._cy-dy,self._cy+dy+1):
            for x in range(self._cx-dx,self._cx+dx+1):
                sx = (x-(self._cx-dx) +1) * TILE_SIZE
                sy = (y-(self._cy-dy) +1) * TILE_SIZE
                elt = Rectangle(Point(sx,sy),
                                Point(sx+TILE_SIZE,sy+TILE_SIZE))
                if self.tile(x,y) == 0:
                    elt = Image(Point(sx,sy),'Resources/tiles.gif')
                if self.tile(x,y) == 1:
                    elt = Image(Point(sx,sy),'Resources/wall.gif')
                if self.tile(x,y) == 2:
                    elt = Image(Point(sx,sy),'Resources/lockers.gif')
                if self.tile(x,y) == 3:
                    elt = Image(Point(sx,sy),'Resources/door.gif')
                if self.tile(x,y) == 4:
                    elt = Image(Point(sx,sy),'Resources/stairs.gif')
                Thing.materialize
                elt.draw(self._window)
        print self._corner

    def redraw (self):
        dx = (VIEWPORT_WIDTH-1)/2
        dy = (VIEWPORT_HEIGHT-1)/2
        for thing in self._things:
            if thing._x >= self._cx - dx and thing._y >= self._cy - dy and thing._x <= self._cx + dx and thing._y <= self._cy + dy:
                self._window.delItem(thing._sprite)
                thing._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),thing._pic)
                self.add(thing,thing._x,thing._y)

    def delete (self,thing):
        self._window.delItem(thing._sprite)
        self._things = [x for x in self._things if x is not t]