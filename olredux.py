from Classes import *
import time
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

def screen_pos (x,y):
    return (x*TILE_SIZE,y*TILE_SIZE)

def screen_pos_index (index):
    x = index % VIEWPORT_WIDTH
    y = (index - x) / VIEWPORT_WIDTH
    return screen_pos(x,y)

def index (x,y):
    return x + (y*LEVEL_WIDTH)

def log (message):
    print time.strftime("[%H:%M:%S]",time.localtime()),message

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

def main ():
    window = GraphWin("Olinland Redux", 
                      WINDOW_WIDTH+WINDOW_RIGHTPANEL, WINDOW_HEIGHT,
                      autoflush=False)

    level = Level()
    log ("level created")

    scr = Screen(level,window,25,25)
    log ("screen created")

    q = EventQueue()

    # ChemTable().materialize(scr,20,20)
    NPC("Pinky","A rat").register(q,40).materialize(scr,30,30)
    NPC("Brain","A rat with a big head").register(q,60).materialize(scr,10,30)

    create_panel(window)

    p = Player("...what's your name, bub?...").materialize(scr,25,25)

    Guitar('guitar','this is guitar').materialize(scr,22,22)

    print scr._things

    q.enqueue(1,CheckInput(window,p))

    while True:
        # Grab the next event from the queue if it's ready
        q.dequeue_if_ready()
        # Time unit = 10 milliseconds
        time.sleep(0.01)
        
if __name__ == '__main__':
    main()
