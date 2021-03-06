from root import *
from graphics import *

# Tile size of the level
LEVEL_WIDTH = 50
LEVEL_HEIGHT = 50

# Tile size of the viewport (through which you view the level)
VIEWPORT_WIDTH = 15
VIEWPORT_HEIGHT = 15

# Pixel size of a tile (which gives you the size of the window)
TILE_SIZE = 50

# Pixel size of the viewport
WINDOW_WIDTH = TILE_SIZE * VIEWPORT_WIDTH
WINDOW_HEIGHT = TILE_SIZE * VIEWPORT_HEIGHT

# Pixel size of the panel on the right where you can display stuff
WINDOW_RIGHTPANEL = 200

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

    def __str__ (self):
        return "<"+self.name()+">"

    def use (self):
        self.com('This thing cannot be used.')

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

    def is_mobile_thing(self):
        return False

    def is_walkable (self):
        return False

    def is_character (self):
        return False

    def com (self,message):
        fg = Rectangle(Point(WINDOW_WIDTH+5,WINDOW_HEIGHT-95),
                               Point(WINDOW_WIDTH+195,WINDOW_HEIGHT-5))
        fg.setFill("white")
        fg.draw(self._screen._window)


        if self.is_character():
            message = self.name()+': \n' + message
        fg = Text(Point(WINDOW_WIDTH+90,
                    WINDOW_HEIGHT-40),message)
        fg.setSize(12)
        fg.setFill("black")
        fg.draw(self._screen._window)

# A helper function that lets you log information to the console
# with some timing information. I found this super useful to 
# debug tricky event-based problems.
#
def log (message):
    print time.strftime("[%H:%M:%S]",time.localtime()),message

