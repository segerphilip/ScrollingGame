from Classes import *
import time
import random

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
    # Sidebar
    fg = Rectangle(Point(WINDOW_WIDTH+1,-20),
                   Point(WINDOW_WIDTH+WINDOW_RIGHTPANEL+20,WINDOW_HEIGHT+20))
    fg.setFill("darkgray")
    fg.setOutline("darkgray")
    fg.draw(window)
    # confidence text
    fg = Text(Point(WINDOW_WIDTH+90,
                25),"Confidence")
    fg.setSize(20)
    fg.setFill("black")
    fg.draw(window)
    # confidence bar
    fg = Rectangle(Point(WINDOW_WIDTH+5,50),
                   Point(WINDOW_WIDTH+195,75))
    fg.setFill("grey")
    fg.setOutline("black")
    fg.draw(window)

def main ():
    window = GraphWin("Olinland Redux", 
                      WINDOW_WIDTH+WINDOW_RIGHTPANEL, WINDOW_HEIGHT,
                      autoflush=False)

    level = Level(0)
    log ("level created")

    scr = Screen(level,window,25,25)
    log ("screen created")

    q = EventQueue()

    create_panel(window)

    p = Player("P-Dawg").materialize(scr,25,25)

    Principal("Mr. Pucella","He looks mad!").register(q,30).materialize(scr,30,10)
    Popular("Pinky","A rat",p).register(q,40).materialize(scr,30,30)
    Popular("Brain","A rat with a big head",p).register(q,60).materialize(scr,10,30)

    Guitar('guitar','this is guitar').materialize(scr,22,22)

    c1 = Chemical('chem1','smells funny','Resources/chem1.gif').materialize(scr,23,23)
    c2 = Chemical('chem2','smells funny','Resources/chem2.gif').materialize(scr,23,24)
    c3 = Chemical('chem3','smells funny','Resources/chem3.gif').materialize(scr,23,25)

    chems = [c1,c2,c3]
    ChemTable(chems).materialize(scr,30,30)

    q.enqueue(1,CheckInput(window,p))

    while True:
        # Grab the next event from the queue if it's ready
        q.dequeue_if_ready()
        # Time unit = 10 milliseconds
        time.sleep(0.01)
        
if __name__ == '__main__':
    main()
