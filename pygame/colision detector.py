import pygame
import random

pygame.init()

screen_hight = 800
screen_width = 600

screen = pygame.display.set_mode((screen_hight,screen_width))
pygame.display.set_caption("colision")

rect_1 = pygame.Rect(0, 0, 40, 40)

obsitacles = []
for _ in range(16):

    obsitcle_rect = pygame.Rect(random.randint(0, 700), random.randint(0,500), 40, 40)
    obsitacles.append(obsitcle_rect)


BG = (50, 50, 50)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.mouse.set_visible(False)

run=True
while run:

    screen.fill(BG)


    col=GREEN
    
    if rect_1.collidelist(obsitacles) >= 0 :
        print(rect_1.collidelist(obsitacles))
        col=RED

    pos =pygame.mouse.get_pos()
    rect_1.center = pos

    pygame.draw.rect(screen, col, rect_1)

    for obstacle in obsitacles:
        pygame.draw.rect(screen, BLUE, obstacle)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
    
    pygame.display.flip()

pygame.quit()