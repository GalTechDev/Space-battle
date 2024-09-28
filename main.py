import GTLib as gt
import pygame as pg
import sys

from menus import *

WINDOWS_SIZE = (900,700)

app = gt.Advanced(size=WINDOWS_SIZE, fps=120, show_fps=True)

@app.event()
def quit(event):
    if event.type == pg.QUIT:
        pg.quit()
        sys.exit()

game = Game(app)

app.call_menu(game)
app.run()