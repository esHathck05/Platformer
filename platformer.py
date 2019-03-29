"""
platformer.py
Author: 
Credit: 
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame

myapp = App()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

blue = Color(0x2EFEC8, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
white = Color(0xFFFFFF, 1.0)
red2 = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue2 = Color(0x0000ff, 1.0)
black2 = Color(0x000000, 1.0)
white2 = Color(0xffffff, 1.0)
grey = Color(0xC0C0C0, 1.0)
blue3 = Color(0xb0e0e6, 1.0)

thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, grey)
blueline = LineStyle(2, blue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)
gridline = LineStyle(1, grey)
grid=RectangleAsset(30,30,gridline,white)

# Background
black = Color(0, 1)
noline = LineStyle(0, black)
bg_asset = RectangleAsset(myapp.width, myapp.height, noline, blue3)
bg = Sprite(bg_asset, (0,0))

# Clouds
cloud = EllipseAsset(100, 60, noline, white)
cloud2 = EllipseAsset(70, 40, noline, white)
Sprite(cloud, (200, 40))
Sprite(cloud2, (500, 160))

# A super wall class for wall-ish behaviors
class GenericWall(Sprite):
    def __init__(self, x, y, w, h, color):
        snapfunc = lambda X : X - X % w
        super().__init__(
            RectangleAsset(w-1,h-1,LineStyle(0,Color(0, 1.0)), color),
            (snapfunc(x), snapfunc(y)))
        # destroy any overlapping walls
        collideswith = self.collidingWithSprites(type(self))
        if len(collideswith):
            collideswith[0].destroy()
            
# Block?
class Wall(GenericWall):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, Color(0, 1.0))
        
class Platformer(App):
    def __init__(self):
        super().__init__()
        self.p = None
        self.pos = (0,0)
        self.listenKeyEvent("keydown", "w", self.newWall)
        self.listenKeyEvent("keydown", "p", self.newPlayer)
        self.listenKeyEvent("keydown", "s", self.newSpring)
        self.listenKeyEvent("keydown", "f", self.newFloor)
        self.listenKeyEvent("keydown", "l", self.newLaser)
        self.listenKeyEvent("keydown", "left arrow", self.moveKey)
        self.listenKeyEvent("keydown", "right arrow", self.moveKey)
        self.listenKeyEvent("keydown", "up arrow", self.moveKey)
        self.listenKeyEvent("keyup", "left arrow", self.stopMoveKey)
        self.listenKeyEvent("keyup", "right arrow", self.stopMoveKey)
        self.listenKeyEvent("keyup", "up arrow", self.stopMoveKey)
        self.listenMouseEvent("mousemove", self.moveMouse)
        self.FallingSprings = []
        self.KillList = []

    def moveMouse(self, event):
        self.pos = (event.x, event.y)
    
    def newWall(self, event):
        Wall(self.pos[0], self.pos[1])
        
    def newPlayer(self, event):
        for p in Platformer.getSpritesbyClass(Player):
            p.destroy()
            self.p = None
        self.p = Player(self.pos[0], self.pos[1], self)
        
    def moveMouse(self, event):
        self.pos = (event.x, event.y)
    
    def newWall(self, event):
        Wall(self.pos[0], self.pos[1])
        
    def newPlayer(self, event):
        for p in Platformer.getSpritesbyClass(Player):
            p.destroy()
            self.p = None
        self.p = Player(self.pos[0], self.pos[1], self)
    
    def newSpring(self, event):
        self.FallingSprings.append(Spring(self.pos[0], self.pos[1], self))
    
    def newFloor(self, event):
        Platform(self.pos[0], self.pos[1])
        
    def newLaser(self, event):
        Turret(self.pos[0], self.pos[1], self)
        
    def moveKey(self, event):
        if self.p:
            self.p.move(event.key)
        
    def stopMoveKey(self, event):
        if self.p:
            self.p.stopMove(event.key)
        
    def step(self):
        if self.p:
            self.p.step()
        for s in self.FallingSprings:
            s.step()
        for t in Platformer.getSpritesbyClass(Turret):
            t.step()
        for b in Platformer.getSpritesbyClass(Bolt):
            b.step()
        for k in self.KillList:
            k.destroy()
        self.KillList = []
            
    def killMe(self, obj):
        if obj in self.FallingSprings:
            self.FallingSprings.remove(obj)
        elif obj == self.p:
            self.p = None
        if not obj in self.KillList:
            self.KillList.append(obj)

myapp.run()