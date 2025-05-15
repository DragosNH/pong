import pygame

pygame.init()

SCREENWIDTH = 900
SCREENHEIGHT = 600
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

pygame.font.init()
calibriBold35 = pygame.font.SysFont("Calibiri Bold", 35)

WHITE = (255, 255, 255)
BGCOLOR = (0, 220, 160)
BLUE = (50, 100, 230)
RED = (230, 50, 100)

player1Y = 250
player2Y = 250
paddleWidth = 15
paddleHeight = 100
p1Points = 0
p2Points = 0

ballX = 450
ballY = 300
ballDx = 4
ballDy = 4

# Hits
hits = 0
last_hit = None


running = True
myClock = pygame.time.Clock()

while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False

    p1Paddle = pygame.Rect(50, player1Y, paddleWidth, paddleHeight)
    p2Paddle = pygame.Rect(820, player2Y, paddleWidth, paddleHeight)
    ball = pygame.Rect(ballX, ballY, 10, 10)

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_z] and player1Y > 0):
        player1Y -=5
    elif(keys[pygame.K_s] and player1Y + paddleHeight < SCREENHEIGHT):
        player1Y += 5

    if (keys[pygame.K_UP] and player2Y > 0):
        player2Y -=5
    elif(keys[pygame.K_DOWN] and player2Y + paddleHeight < SCREENHEIGHT):
        player2Y += 5
     
    ballX += ballDx
    ballY += ballDy

    if ball.colliderect(p1Paddle):
        ballDx = abs(ballDx)
    if ball.colliderect(p2Paddle):
        ballDx = -abs(ballDx)

    # Hits
    if ball.colliderect(p1Paddle) and last_hit != 'p1':
        last_hit = 'p1'

    elif ball.colliderect(p2Paddle) and last_hit == 'p1':
        hits += 1
        last_hit = 'p2'

    if ballX <= 0 or ballX >= SCREENWIDTH:
        last_hit = None


    if hits % 5 == 0 and hits != 0:
        if ballDx > 0:
            ballDx += 1
        else:
            ballDx -= 1

        if ballDy > 0:
            ballDy += 1
        else:
            ballDy -= 1

        hits = 0


    elif ballY <= 0:
        ballDy = abs(ballDy)
    elif ballY >= SCREENHEIGHT:
        ballDy = -abs(ballDy)
    elif ballX >= SCREENWIDTH or ballX <= 0:
        if ballX >= SCREENWIDTH:
            p1Points +=1
        elif ballX <= 0:
            p2Points += 1
        ballX = 450
        ballY = 300
        player1Y1 = 250
        player2Y2 = 250

    screen.fill(BGCOLOR)

    hits_text = calibriBold35.render(f"Hits: {hits}", True, BLUE)
    screen.blit(hits_text, (SCREENWIDTH // 2 - 40, 20))

    pygame.draw.rect(screen, BLUE, p1Paddle)
    pygame.draw.rect(screen, RED, p2Paddle)
    pygame.draw.rect(screen, WHITE, ball)
    p1PtsTxt = calibriBold35.render("P1 POINTS: " + str(p1Points), True, BLUE)
    p2PtsTxt = calibriBold35.render("P2 POINTS: " +str(p2Points), True, RED)
    screen.blit(p1PtsTxt, (130, 20))
    screen.blit(p2PtsTxt, (620, 20))


    pygame.display.flip() 
    myClock.tick(60)

quit()