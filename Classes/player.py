from character import *
from screen import *
from level import *

#
# The Player character
#
class Player (Character):
    def __init__ (self,name):
        Character.__init__(self,name,"Yours truly")
        log("Player.__init__ for "+str(self))
        self._pics = ['Resources/PhilL.gif', 'Resources/Phil.gif', 'Resources/PhilR.gif', 'Resources/Phil.gif']
        self._ind = 1
        self._pic = self._pics[self._ind]
        self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)
        self._confidence = 0
        self._inventory = []
        self._stairs = False
        self._leveled = False

    def is_player (self):
        return True

    # The move() method of the Player is called when you 
    # press movement keys. 
    # It is different enough from movement by the other
    # characters that you'll probably need to overwrite it.
    # In particular, when the Player move, the screen scrolls,
    # something that does not happen for other characters

    def move (self,dx,dy):
        if self._ind != 3:
            self._ind += 1
            self._pic = self._pics[self._ind]
        else:
            self._ind = 0
            self._pic = self._pics[self._ind]
        tx = self._x + dx
        ty = self._y + dy
        if tx > 1 and ty > 1 and tx < LEVEL_WIDTH and ty < LEVEL_HEIGHT:
            if self._screen.tile(tx,ty) != 2 and self._screen.tile(tx,ty) != 1:
                for thing in self._screen._things:
                    if thing._x == tx and thing._y == ty and not thing.is_walkable():
                        return
                self._x = tx
                self._y = ty
                self._sprite.move(dx*TILE_SIZE,dy*TILE_SIZE)
                # self._screen._window.delItem(self._sprite)
                # self._sprite = Image(Point(TILE_SIZE/2,TILE_SIZE/2),self._pic)
                # self._screen.add(self,self._x,self._y)
                if tx > 11 and tx < 40 and ty > 11 and ty < 40:
                    self._screen.scroll(dx,dy)
                    self._screen.redraw()
                if (tx < 11 or tx > 40) and (ty < 11 or ty > 40):
                    self._screen.redraw()
                elif (tx < 11 or tx > 40) and dy != 0:
                    self._screen.scroll(dx,dy)
                    self._screen.redraw()
                elif (ty < 11 or ty > 40) and dx != 0:
                    self._screen.scroll(dx,dy)
                    self._screen.redraw()
            self._screen._window.update()

    def interact (self):
        if (self._x > 20 and self._x < 29) and (self._y > 4 and self._y <= 8):
            if not self._stairs:
                self._stairs = True
                self._leveled = True
                level1 = Level(1)
                log ("second level created")
                self._screen2 = Screen(level1,self._screen._window,self._x,11)
                self._screen1 = self._screen
                self._screen = self._screen2
                self._screen._window.redraw()
                # self._screen.delete(self)
                # self._screen.add(self,self._x,self._y)
                # populate with objects/people
            else:
                if self._leveled:
                    self._screen = self._screen1
                    self._leveled = False
                else:
                    self._screen = self._screen2
                    self._leveled = True
        for t in self._screen._things:
            if ( (t._x == self._x + 1 or t._x == self._x - 1) and t._y == self._y) or ((t._y == self._y + 1 or t._y == self._y - 1) and t._x == self._x):
                if t.is_thing():
                    if t.is_mobile_thing():
                        t.take(self)
                        return
                    t.use(self)
                if t.is_character():
                    t.talk()

    def update_confidence (self):
        if self._confidence <= 10:
            fg = Rectangle(Point(WINDOW_WIDTH+5,50),
                           Point(WINDOW_WIDTH+self._confidence*19,75))
            fg.setFill("red")
            fg.draw(self._screen._window)

    def inventory (self):
        return self._inventory

    def have_thing (self,t):
        for c in self.inventory():
            if c is t:
                return True
        return False