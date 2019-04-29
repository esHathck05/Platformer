from ggame import App, Sprite, RectangleAsset, CircleAsset, LineStyle, Color
from math import pi

myapp = App()

black = Color(0, 1)
noline = LineStyle(0, black)
yellow = Color(0xffff00, 1)

myapp = App()

# define colors and line style
black = Color(0, 1)
noline = LineStyle(0, black)
# a rectangle asset and sprite to use as background
bg_asset = RectangleAsset(myapp.width, myapp.height, noline, black)
bg = Sprite(bg_asset, (0,0))

class Pacman(Sprite):
    def __init__(self, x, y, w, h, color, app):
        super().__init__(CircleAsset(30, LineStyle(0,Color(0, 1.0)), color))
        self.xdirection = 4
        self.ydirection = 4
        self.go = True
            
    def move(self, key):
        if key == "left arrow":
            self.xdirection = -4

        elif key == "right arrow":
            self.xdirection = 4
                
        elif key == "up arrow":
            self.ydirection = -4
            
        elif key == "down arrow":
            self.ydirection = 4


# Set up event handlers for the app
class Twoplayer(App):
    def __init__(self):
        super().__init__()
        self.pac = Pacman(50, 50, 10, 10, yellow, self)
        myapp.listenKeyEvent('keydown', 'left arrow', self.moveKey)
        myapp.listenKeyEvent('keydown', 'right arrow', self.moveKey)
        myapp.listenKeyEvent('keydown', 'up arrow', self.moveKey)

    def step(self):
        self.pac.x += self.pac.xdirection 
        if self.pac.x + self.pac.width > myapp.width:
            self.pac.x -= self.pac.xdirection
            left(Pacman)
        if self.pac.x < 0:
            right(Pacman)
        
        self.pac.y += self.pac.ydirection
        if self.pac.y + self.pac.height > myapp.height:
            self.pac.y -= self.pac.ydirection
            down(Pacman)
        if self.pac.y < 0:
            up(Pacman)
    
    # handles directions
    def moveKey(self, event):
        if self.pac:
            self.pac.move(event.key)
            
    def leftKey(event):
        left(Pacman)
        
    def rightKey(event):
        right(Pacman)

app = Twoplayer()
app.run()print("Hello, world.")