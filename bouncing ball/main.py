import pygame
import sys
WIDTH = 400
HEIGHT = 500
black = 0,0,0
speed = [2,2]


pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
ball = pygame.image.load("ball.jpg")
ballrect=ball.get_rect()
#pygame.display.get_caption("Snake")
clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > WIDTH:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > HEIGHT:
        speed[1] = -speed[1]


    screen.fill(black)  
    screen.blit(ball, ballrect)      
    pygame.display.update()
    clock.tick(60)