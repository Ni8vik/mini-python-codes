import pygame
import random
import os
print(os.getcwd())
pygame.init()

screen_hight = 800
screen_width = 600

screen = pygame.display.set_mode((screen_hight,screen_width))
pygame.display.set_caption("colision")


obsitacles = []
for _ in range(16):
    obsitcle_rect = pygame.Rect(random.randint(0, 700), random.randint(0,500), 40, 40)
    obsitacles.append(obsitcle_rect)

line_start=(screen_width / 2 , screen_hight / 2)


BG = (50, 50, 50)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


run=True
while run:

    screen.fill(BG)

    pos = pygame.mouse.get_pos()
    pygame.draw.line(screen, WHITE, line_start, pos, 5)
    pygame.draw.circle(screen, (255, 255, 150), pos, 10, 5)
    for obstacle in obsitacles:
        if obstacle.clipline((line_start, pos)):
            pygame.draw.rect(screen, RED, obstacle)
        else:
             pygame.draw.rect(screen, BLUE, obstacle)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
    
    pygame.display.flip()

pygame.quit()