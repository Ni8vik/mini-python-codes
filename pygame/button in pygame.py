import pygame
import buttonpygameclass as button

pygame.init()


screen_width = 1300
screen_hight = 700


#create game window
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("butten demo")

#loadin image
start_img = pygame.image.load("play button.jfif").convert_alpha()
exit_img = pygame.image.load("exit button.jpg").convert_alpha()

#button class

    
#create button instances
start_button = button.button(100, 200, start_img, 0.5)
exit_button = button.button(600, 200, exit_img, 0.3)

#game loop
run=True
while run:
    
    screen.fill((202, 228, 241))

    if start_button.draw(screen) == True:
         print("think this is starting")
    if exit_button.draw(screen) == True:
         run = False


    #event handler
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
    
    pygame.display.update()

pygame.quit()
