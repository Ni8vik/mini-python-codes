import pygame


pygame.init()


screen_width = 1300
screen_hight = 700


#create game window
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("flappy bird")

#player information
PLAYER_X = 500
PLAYER_Y = 500
PLAYER_WIDTH = 60
PLAYER_HIGHT = 60
VELOSITY = 5

#colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#game loop
run=True
while run:
    
    pygame.time.delay(100)

    screen.fill((202, 228, 241))

    KEYS = pygame.key.get_pressed()

    if KEYS[pygame.K_w]:
         PLAYER_Y -= VELOSITY
    if KEYS[pygame.K_s]:
         PLAYER_Y += VELOSITY
    if KEYS[pygame.K_a]:
         PLAYER_X += VELOSITY
    if KEYS[pygame.K_d]:
         PLAYER_X -= VELOSITY 

    #event handler
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

    pygame.draw.rect(screen, RED, (PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HIGHT))
    pygame.display.update()

pygame.quit()
