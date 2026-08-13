import pygame

class button():
    def __init__(self, x, y, image, sclae):
        width = image.get_width()
        hight = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * sclae), int(hight * sclae)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action =  False
        #get mouse positon
        pos = pygame.mouse.get_pos()

        #check mouse ovet button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
             self.clicked = False    

        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))


        return action