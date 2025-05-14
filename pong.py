from pygame import *

SCREENWIDTH = 9000
SCREENHEIGHT = 600
screen = display.set_mode((SCREENWIDTH, SCREENHEIGHT))

WHITE = (255, 255, 255)
BGCOLOR = (0, 220, 160)
BLUE = (50, 100, 230)
RED = (230, 50, 100)

running = True
myClock = time.Clock()

while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    screen.fill(BGCOLOR)

    display.flip()
    myClock.tick(60)

quit()