import pygame
import random

pygame.init()

screen_hight = 800
screen_width = 600

screen = pygame.display.set_mode((screen_hight,screen_width))
pygame.display.set_caption("colision")


obsitacles = []
for _ in range(16):

    obsitcle_rect = pygame.Rect(random.randint(0, 700), random.randint(0,500), 40, 40)
    obsitacles.append(obsitcle_rect)


BG = (50, 50, 50)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



run=True
while run:

    screen.fill(BG)

    pos = pygame.mouse.get_pos()

    for obstacle in obsitacles:
        if obstacle.collidepoint(pos):
            pygame.draw.rect(screen, RED, obstacle)
        else:
             pygame.draw.rect(screen, BLUE, obstacle)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
    
    pygame.display.flip()

pygame.quit()