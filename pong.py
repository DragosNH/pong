import pygame

pygame.init()

SCREENWIDTH = 900
SCREENHEIGHT = 600
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))


WHITE = (255, 255, 255)
BGCOLOR = (0, 220, 160)
BLUE = (50, 100, 230)
RED = (230, 50, 100)

running = True
myClock = pygame.time.Clock()

while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False
    screen.fill(BGCOLOR)

    pygame.display.flip() 
    myClock.tick(60)

quit()