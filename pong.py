import pygame

pygame.init()

SCREENWIDTH = 900
SCREENHEIGHT = 600
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

WHITE = (255, 255, 255)
BGCOLOR = (0, 220, 160)
BLUE = (50, 100, 230)
RED = (230, 50, 100)

player1Y = 250
player2Y = 250
paddleWidth = 30
paddleHeight = 100

running = True
myClock = pygame.time.Clock()

while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False

    p1Paddle = pygame.Rect(50, player1Y, paddleWidth, paddleHeight)
    p2Paddle = pygame.Rect(850, player2Y, paddleWidth, paddleHeight)

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_z] and player1Y > 0):
        player1Y -=5
    elif(keys[pygame.K_s] and player1Y + paddleHeight < SCREENHEIGHT):
        player1Y += 5

    if (keys[pygame.K_UP] and player2Y > 0):
        player2Y -=5
    elif(keys[pygame.K_DOWN] and player2Y + paddleHeight < SCREENHEIGHT):
        player2Y += 5
     

    screen.fill(BGCOLOR)

    pygame.draw.rect(screen, BLUE, p1Paddle)
    pygame.draw.rect(screen, RED, p2Paddle)

    pygame.display.flip() 
    myClock.tick(60)

quit()