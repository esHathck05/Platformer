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

#Clouds
cloud = EllipseAsset(100, 60, noline, white)
Sprite(cloud, ()

myapp.run()