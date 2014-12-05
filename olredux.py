############################################################
#
# Olinland Redux
#
# Scaffolding to the final project for Game Programming
# Devs: Chelsea, Philip
#

import time
import random
from graphics import *


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

RAT_DELAY = 10

MOVES = [(1,0), (-1,0),
         (0,1), (0,-1),
         (0,0)]

def screen_pos (x,y):
    return (x*TILE_SIZE,y*TILE_SIZE)

def screen_pos_index (index):
    x = index % VIEWPORT_WIDTH
    y = (index - x) / VIEWPORT_WIDTH
    return screen_pos(x,y)

def index (x,y):
    return x + (y*LEVEL_WIDTH)


#############################################################
# 
# The class hierarchy for objects that you can interact with
# in the world
#
# Roughly modeled from the corresponding hierarchy in our
# adventure game
#


#
# The root object
#
class Root (object):
    # default predicates

    # is this object a Thing?
    def is_thing (self):
        return False

    # is this object a Character?
    def is_character (self):
        return False

    # is this object the Player?
    def is_player (self):
        return False

    # can this object be walked over during movement?
    def is_walkable (self):
        return False


# A thing is something that can be interacted with and by default
# is not moveable or walkable over
#
#   Thing(name,description)
#
# A thing defines a default sprite in field _sprite
# To create a new kind of thing, subclass Thing and 
# assign it a specific sprite (see the OlinStatue below).
# 
class Thing (Root):
    def __init__ (self,name,desc):
        self._name = name
        self._description = desc
        self._sprite = Text(Point(TILE_SIZE/2,TILE_SIZE/2),"?")
        log("Thing.__init__ for "+str(self))

    def __str__ (self):
        return "<"+self.name()+">"

    # return the sprite for display purposes
    def sprite (self):
        return self._sprite

    # return the name
    def name (self):
        return self._name

    # return the position of the thing in the level array
    def position (self):
        return (self._x,self._y)
        
    # return the description
    def description (self):
        return self._description

    # creating a thing does not put it in play -- you have to 
    # call materialize, passing in the screen and the position
    # where you want it to appear
    def materialize (self,screen,x,y):
        screen.add(self,x,y)
        self._screen = screen
        self._x = x
        self._y = y
        self._screen._things.append(self)
        return self

    def is_thing (self):
        return True

    def is_walkable (self):
        return False


#
# Example of a kind of thing with its specific sprite
# (here, a rather boring gray rectangle.)
#
class OlinStatue (Thing):
    def __init__ (self):
        Thing.__init__(self,"Olin statue","A statue of F. W. Olin")
        self._pic = 'rat.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)


#
# Characters represent persons and animals and things that move
# about possibly proactively
#
class Character (Thing):
    def __init__ (self,name,desc):
        Thing.__init__(self,name,desc)
        log("Character.__init__ for "+str(self))
        rect = Rectangle(Point(1,1),
                         Point(TILE_SIZE-1,TILE_SIZE-1))
        rect.setFill("red")
        rect.setOutline("red")
        self._sprite = rect

    # A character has a move() method that you should implement
    # to enable movement

    def move (self,dx,dy):
        tx = self._x + dx
        ty = self._y + dy
        if tx > 1 and ty > 1 and tx < LEVEL_WIDTH and ty < LEVEL_HEIGHT:
            if self._screen.tile(tx,ty) != 2:
                for thing in self._screen._things:
                    if thing._x == tx and thing._y == ty and not thing.is_walkable():
                        return
                self._x = tx
                self._y = ty
                self._sprite.move(dx*TILE_SIZE,dy*TILE_SIZE)
        self._screen._window.update()

    def is_character (self):
        return True

    def is_walkable (self):
        return False


# 
# A Rat is an example of a character which defines an event that makes
# the rat move, so that it can be queued into the event queue to enable
# that behavior. (Which is right now unfortunately not implemented.)
#
class Rat (Character):
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

#
# The Player character
#
class Player (Character):
    def __init__ (self,name):
        Character.__init__(self,name,"Yours truly")
        log("Player.__init__ for "+str(self))
        self._pic = 't_android.gif'
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)

    def is_player (self):
        return True

    # The move() method of the Player is called when you 
    # press movement keys. 
    # It is different enough from movement by the other
    # characters that you'll probably need to overwrite it.
    # In particular, when the Player move, the screen scrolls,
    # something that does not happen for other characters

    def move (self,dx,dy):
        tx = self._x + dx
        ty = self._y + dy
        if tx > 1 and ty > 1 and tx < LEVEL_WIDTH and ty < LEVEL_HEIGHT:
            if self._screen.tile(tx,ty) != 2:
                for thing in self._screen._things:
                    if thing._x == tx and thing._y == ty and not thing.is_walkable():
                        return
                self._x = tx
                self._y = ty
                self._sprite.move(dx*TILE_SIZE,dy*TILE_SIZE)
                if tx > 11 and tx < 40 and ty > 11 and ty < 40:
                    self._screen.scroll(dx,dy)
                    self._screen.redraw()
                if (tx < 11 or tx > 40) and (ty < 11 or ty > 40):
                    pass
                elif (tx < 11 or tx > 40) and dy != 0:
                    self._screen.scroll(dx,dy)
                    self._screen.redraw()
                elif (ty < 11 or ty > 40) and dx != 0:
                    self._screen.scroll(dx,dy)
                    self._screen.redraw()
            self._screen._window.update()

#############################################################
# 
# The description of the world and the screen which displays
# the world
#
# A level contains the background stuff that you can't really
# interact with. The tiles are decorative, and do not come
# with a corresponding object in the world. (Though you can
# change that if you want.)
#
# Right now, a level is described using the following encoding
#
# 0 empty   (light green rectangle)
# 1 grass   (green rectangle)
# 2 tree    (sienna rectangle)
#
# you'll probably want to make nicer sprites at some point.


#
# This implements a random level right now. 
# You'll probably want to replace this with something that 
# implements a specific map -- perhaps of Olin?
#
class Level (object):
    def __init__ (self):
        size = LEVEL_WIDTH * LEVEL_HEIGHT
        map = [0] * size
        for i in range(100):
            map[random.randrange(size)] = 1
        for i in range(50):
            map[random.randrange(size)] = 2
        self._map = map

    def _pos (self,x,y):
        return x + (y*LEVEL_WIDTH);

    # return the tile at a given tile position in the level
    def tile (self,x,y):
        return self._map[self._pos(x,y)]

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
                sx = (x-(cx-dx)) * TILE_SIZE
                sy = (y-(cy-dy)) * TILE_SIZE
                elt = Rectangle(Point(sx,sy),
                                Point(sx+TILE_SIZE,sy+TILE_SIZE))
                if self.tile(x,y) == 0:
                    elt.setFill('lightgreen')
                    elt.setOutline('lightgreen')
                if self.tile(x,y) == 1:
                    elt.setFill('green')
                    elt.setOutline('green')
                elif self.tile(x,y) == 2:
                    elt.setFill('sienna')
                    elt.setOutline('sienna')
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
                sx = (x-(self._cx-dx)) * TILE_SIZE
                sy = (y-(self._cy-dy)) * TILE_SIZE
                elt = Rectangle(Point(sx,sy),
                                Point(sx+TILE_SIZE,sy+TILE_SIZE))
                if self.tile(x,y) == 0:
                    elt.setFill('lightgreen')
                    elt.setOutline('lightgreen')
                if self.tile(x,y) == 1:
                    elt.setFill('green')
                    elt.setOutline('green')
                elif self.tile(x,y) == 2:
                    elt.setFill('sienna')
                    elt.setOutline('sienna')
                Thing.materialize
                elt.draw(self._window)
        print self._corner

    def redraw (self):
        dx = (VIEWPORT_WIDTH-1)/2
        dy = (VIEWPORT_HEIGHT-1)/2
        for thing in self._things:
            if thing._x >= self._cx - dx and thing._y >= self._cy - dy and thing._x <= self._cx + dx and thing._y <= self._cy + dy:
                # (sx,sy) = screen_pos(thing._x,thing._y)
                self._window.delItem(thing._sprite)
                thing._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),thing._pic)
                self.add(thing,thing._x,thing._y)
                # thing._sprite.draw(self._window)
                # self._window.redraw()

# A helper function that lets you log information to the console
# with some timing information. I found this super useful to 
# debug tricky event-based problems.
#
def log (message):
    print time.strftime("[%H:%M:%S]",time.localtime()),message

    

#############################################################
# 
# The event queue
#
# An event is any object that implements an event() method
# That event method gets the event queue as input, so that
# it can add to the event queue if it needs to.

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


# A simple event class that checks for user input.
# It re-enqueues itself after the check.

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
        key = self._window.checkKey()
        if key == 'q':
            self._window.close()
            exit(0)
        if key in MOVE:
            (dx,dy) = MOVE[key]
            self._player.move(dx,dy)
        q.enqueue(1,self)


#
# Create the right-side panel that can be used to display interesting
# information to the player
#
def create_panel (window):
    fg = Rectangle(Point(WINDOW_WIDTH+1,-20),
                   Point(WINDOW_WIDTH+WINDOW_RIGHTPANEL+20,WINDOW_HEIGHT+20))
    fg.setFill("darkgray")
    fg.setOutline("darkgray")
    fg.draw(window)
    fg = Text(Point(WINDOW_WIDTH+100,
                    30),"Olinland Redux")
    fg.setSize(24)
    fg.setStyle("italic")
    fg.setFill("red")
    fg.draw(window)


#
# The main function
# 
# It initializes everything that needs to be initialized
# Order is important for graphics to display correctly
# Note that autoflush=False, so we need to explicitly
# call window.update() to refresh the window when we make
# changes
#
def main ():

    window = GraphWin("Olinland Redux", 
                      WINDOW_WIDTH+WINDOW_RIGHTPANEL, WINDOW_HEIGHT,
                      autoflush=False)

    level = Level()
    log ("level created")

    scr = Screen(level,window,25,25)
    log ("screen created")

    q = EventQueue()

    OlinStatue().materialize(scr,20,20)
    Rat("Pinky","A rat").register(q,40).materialize(scr,30,30)
    Rat("Brain","A rat with a big head").register(q,60).materialize(scr,10,30)

    create_panel(window)

    p = Player("...what's your name, bub?...").materialize(scr,25,25)

    print scr._things

    q.enqueue(1,CheckInput(window,p))

    while True:
        # Grab the next event from the queue if it's ready
        q.dequeue_if_ready()
        # Time unit = 10 milliseconds
        time.sleep(0.01)



if __name__ == '__main__':
    main()
