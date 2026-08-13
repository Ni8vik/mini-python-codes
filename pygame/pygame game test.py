import pygame


pygame.init()


screen_width = 850
screen_hight = 480




#create game window
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("game ")

clock = pygame.time.Clock()
music = pygame.mixer.music.load("game/music.mp3")
pygame.mixer.music.play(-1)

score= 0 

#player images sprite
walkright = [pygame.image.load("game/R1.png"), pygame.image.load("game/R2.png"),
                       pygame.image.load("game/R3.png"),pygame.image.load("game/R4.png"),
                       pygame.image.load("game/R5.png"),pygame.image.load("game/R6.png"),
                       pygame.image.load("game/R7.png"),pygame.image.load("game/R8.png"),
                       pygame.image.load("game/R9.png")]

walkleft = [pygame.image.load("game/L1.png"), pygame.image.load("game/L2.png"),
                       pygame.image.load("game/L3.png"),pygame.image.load("game/L4.png"),
                       pygame.image.load("game/L5.png"),pygame.image.load("game/L6.png"),
                       pygame.image.load("game/L7.png"),pygame.image.load("game/L8.png"),
                       pygame.image.load("game/L9.png")]

bg = pygame.image.load("game/bg.jpg")
char = pygame.image.load("game/standing.png")



#player class
class player(object):
    def __init__(self, x, y, width, hight, ):
            self.x = x
            self.y = y
            self.width = width
            self.hight = hight
            self.vel = 6
            self.isjump = False
            self.jumpcount = 10
            self.left = False
            self.right = False
            self.walkcount = 0 
            self.standing = True
            self.hitbox =  (self.x + 17, self.y + 11, 28, 52)

    def draw(self, screen):
              
        if self.walkcount + 1 >= 27:
            self.walkcount = 0
        if not(self.standing):
            if self.left:
                screen.blit(walkleft[self.walkcount//3], (self.x, self.y))
                self.walkcount += 1

            elif self.right:
                screen.blit(walkright[self.walkcount//3], (self.x, self.y))
                self.walkcount += 1
            
        else:
            if self.right:
                screen.blit(walkright[0], (self.x, self.y))
            else:
                screen.blit(walkleft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 28, 52)
        #pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        self.isjump = False
        self.jumpcount = 10 
        self.x = 60
        self.y = 410
        self.walkcount = 0
        font_hited = pygame.font.SysFont("bold", 100)
        text1 = font_hited.render("you have been hit", 1, (0, 0, 255))
        screen.blit(text1, (425 - (text1.get_width()/2), 220))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()
                if score <= -15:
                    pygame.quit()


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, screen):
        pygame.draw.circle(screen, (self.color), (self.x, self.y), self.radius)

#enemies class
class enemies(object):

    walkRight = [pygame.image.load("game/R1E.png"),pygame.image.load("game/R2E.png"),pygame.image.load("game/R3E.png")
                  ,pygame.image.load("game/R4E.png"),pygame.image.load("game/R5E.png"),pygame.image.load("game/R6E.png")
                  ,pygame.image.load("game/R7E.png"),pygame.image.load("game/R8E.png"),pygame.image.load("game/R9E.png")
                  ,pygame.image.load("game/R10E.png"),pygame.image.load("game/R11E.png")]
    
    walkleft = [pygame.image.load("game/L1E.png"),pygame.image.load("game/L2E.png"),pygame.image.load("game/L3E.png")
                 ,pygame.image.load("game/L4E.png"),pygame.image.load("game/L5E.png"),pygame.image.load("game/L6E.png")
                 ,pygame.image.load("game/L7E.png"),pygame.image.load("game/L8E.png"),pygame.image.load("game/L9E.png")
                 ,pygame.image.load("game/L10E.png"),pygame.image.load("game/L11E.png")]
    goblindie = [pygame.image.load("game/goblindieimage.jfif")]

    def __init__(self, x, y, width, hight, end):
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.end = end
        self.path = [self.x, self.end]
        self.walkcount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True


    def draw(self, screen):
        self.move()
        if self.visible:
            if self.walkcount + 1 >= 33:
                self.walkcount = 0

            if self.vel > 0:
                screen.blit(self.walkRight[self.walkcount // 3], (self.x, self.y))
                self.walkcount += 1
            else:
                screen.blit(self.walkleft[self.walkcount // 3], (self.x, self.y))
                self.walkcount += 1
        

            pygame.draw.rect(screen, (RED), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(screen, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - ((50/10) * (10 - self.health)), 10))
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        #pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0
    
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print("goblin has been hitted")
            
            
                
        
        

#colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

#pygame drawing
def redraw_game_window():
    screen.blit(bg, (0, 0))
    text = font.render("Score : " + str(score), 1, (0, 0, 0))
    screen.blit(text, (730, 20))
    man.draw(screen)
    goblin.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.update()

font = pygame.font.SysFont("italic", 30, True)
bullets = []
man = player(300, 410, 64, 64)
shootloop = 0
goblin = enemies(200, 410, 64, 64, 550)

#game loop
run=True
while run:
    
    clock.tick(27)

    if goblin.visible == True:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                    man.hit()
                    score -= 5

    if shootloop > 0:
        shootloop +=1
    if shootloop > 3:
        shootloop = 0

    #event handler
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
    
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                score += 1 
                bullets.pop(bullets.index(bullet))

        if bullet.x < 850 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    #move code block
    KEYS = pygame.key.get_pressed()
    if pygame.mouse.get_pressed() [0] and  shootloop == 0 :
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5 :
            bullets.append(projectile(round(man.x + man.width // 2), round(man.y + man.hight // 2), 6, (BLACK), facing))

        shootloop = 1

    if KEYS[pygame.K_a] and man.x > man.vel:
            man.x -= man.vel
            man.left= True
            man.right = False 
            man.standing = False  

    elif KEYS[pygame.K_d] and man.x < 850 - man.width - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing = False
            
    else:
        man.standing = True
        man.walkcount = 0

    if not(man.isjump):
        if KEYS[pygame.K_SPACE]:
            man.isjump = True
            man.left = False
            man.right= False
            man.walkcount = 0
    else:
        if man.jumpcount >= -10:
            neg = 1
            if man.jumpcount < 0:
                neg = -1
            man.y -= (man.jumpcount ** 2) * 0.6 * neg
            man.jumpcount -= 1
        else:
            man.isjump = False
            man.jumpcount = 10
    
    redraw_game_window()


pygame.quit()
