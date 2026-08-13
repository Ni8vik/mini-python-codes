import pygame
import math


pygame.init()

clock = pygame.time.Clock()
FPS = 60

screen_width = 1300
screen_hight = 600


#create game window
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("endless scrollin bg")

#load image
bg = pygame.image.load("pygame bg.png").convert()
bg_width = bg.get_width()
bg_rect = bg.get_rect()

#define game var
scroll = 0
tiles = math.ceil(screen_width / bg_width) + 1


#game loop
run=True
while run:
    
    clock.tick(FPS)

    #draw scrolling bg
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
        bg_rect.x = i * bg_width + scroll
        pygame.draw.rect(screen, (255, 0, 0), bg_rect, 1)
    #scroll bg
    scroll -= 5

    #reset scroll
    if abs(scroll) > bg_width :
        scroll = 0
    
    #event handler
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
    
    pygame.display.update()

pygame.quit()
