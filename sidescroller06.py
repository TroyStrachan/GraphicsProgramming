import pygame, random
pygame.init()
#TRANSPARENCY = (0,0,0,0)
screen = pygame.display.set_mode((640, 480))

#Link running
class Link(pygame.sprite.Sprite):
    
    def __init__(self, screen):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("link01.png")
        self.image = self.image.convert()
        tranColor = self.image.get_at((1, 1))
        self.image.set_colorkey(tranColor)
        self.rect = self.image.get_rect()
        self.rect.center = (320, 240)
        self.img = []
# link running        
        self.loadPics()
#        self.loaddeadpics()
#        self.loadattackpics()
        self.frame = 0
        self.delay = 3
        self.pause = self.delay
        self.dx = 4    
          
# loading sound mixer
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init()
            self.sndYay = pygame.mixer.Sound("yay.ogg")
            self.sndThunder = pygame.mixer.Sound("thunder.ogg")
            self.sndEngine = pygame.mixer.Sound("engine.ogg")
            self.sndEngine.play(-1)


    def update(self):
        
#        mousex, mousey = pygame.mouse.get_pos()
#        if mousey < 150:
#            mousey= 150
        self.rect.center = (100, 375)
        self.pause -= 1
        if self.pause <= 0:
            self.pause = self.delay
            
        self.frame += 1
        if self.frame > 2:
            self.frame = 0
            
        self.image = self.img[self.frame]
            
        self.rect.centerx += self.dx
        if self.rect.centerx > self.screen.get_width():
            self.rect.centerx = 0
    
    def loadPics(self):
        for i in range(3):
            imgName = "link0{0}.png".format(i)
            tmpImg = pygame.image.load(imgName)
            tmpImg.convert()
            tranColor = tmpImg.get_at((0, 0))
            tmpImg.set_colorkey(tranColor)
            self.img.append(tmpImg)
            
    def loadattackpics(self):
        for i in range(9):
            imgName = "linkattack0{0}.png".format(i)
            tmpImg = pygame.image.load(imgName)
            tmpImg.convert()
            tranColor = tmpImg.get_at((0, 0))
            tmpImg.set_colorkey(tranColor)
            self.img.append(tmpImg)
            
    def loaddeadpics(self):
        for i in range(5):
            imgName = "linkdead0{0}.png".format(i)
            tmpImg = pygame.image.load(imgName)
            tmpImg.convert()
            tranColor = tmpImg.get_at((0, 0))
            tmpImg.set_colorkey(tranColor)
            self.img.append(tmpImg)

#scrolling background           
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Landscape-with-treeslong1.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = -2
        self.reset()
        
    def update(self):
        self.rect.left += self.dx
        if self.rect.left >= 0:
            self.reset() 
    
    def reset(self):
        self.rect.bottom = screen.get_height()

# scrolling foreground        
class Foreground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("hedgeslong.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.dx = -2
        self.reset()
        
    def update(self):
        self.rect.left += self.dx
        if self.rect.left >= 0:
            self.reset() 
    
    def reset(self):
        self.rect.bottom = screen.get_height()            
        
#enemy 1
class Peter(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy010.png")
        self.image = self.image.convert()
        tranColor = self.image.get_at((1, 1))
        self.image.set_colorkey(tranColor)
        self.rect = self.image.get_rect()
        self.rect.center = (320, 240)
        self.img = []
        
        self.loadPics()
        self.frame = 0
        self.delay = 3
        self.pause = self.delay
        self.dx = -2      

    def update(self):
        self.rect.center = (600, 375)
        self.pause -= 1
        if self.pause <= 0:
            self.pause = self.delay
            
        self.frame += 1
        if self.frame > 4:
            self.frame = 0
            
        self.image = self.img[self.frame]
            
        self.rect.centerx += self.dx
        if self.rect.centerx > self.screen.get_width():
            self.rect.centerx = 0
    
    def loadPics(self):
        for i in range(5):
            imgName = "enemy01{0}.png".format(i)
            tmpImg = pygame.image.load(imgName)
            tmpImg.convert()
            tranColor = tmpImg.get_at((0, 0))
            tmpImg.set_colorkey(tranColor)
            self.img.append(tmpImg)
            
    def reset(self):
        self.rect.left = -960

#enemy 2           
class Brian(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy020.png")
        self.image = self.image.convert()
        tranColor = self.image.get_at((1, 1))
        self.image.set_colorkey(tranColor)
        self.rect = self.image.get_rect()
        self.rect.center = (320, 240)
        self.img = []
        
        self.loadPics()
        self.frame = 0
        self.delay = 10
        self.pause = self.delay
        self.dx = 0  

    def update(self):
        self.rect.center = (600, 375)
        self.pause += 0
        if self.pause <= 0:
            self.pause = self.delay
            
        self.frame += 1
        if self.frame > 5:
            self.frame = 0
            
        self.image = self.img[self.frame]
            
        self.rect.centerx += self.dx
        if self.rect.centerx > self.screen.get_width():
            self.rect.centerx = 0
    
    def loadPics(self):
        for i in range(13):
            imgName = "enemy02{0}.png".format(i)
            tmpImg = pygame.image.load(imgName)
            tmpImg.convert()
            tranColor = tmpImg.get_at((0, 0))
            tmpImg.set_colorkey(tranColor)
            self.img.append(tmpImg)

    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.dy = random.randrange(5, 10)
        self.dx = random.randrange(-2, 2)
            
class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 3
        self.score = 0
        self.font = pygame.font.SysFont("None", 50)
        
    def update(self):
        self.text = "planes: %d, score: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()
            
def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Link Running")
    
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    enemy1 = Peter(screen)
    enemy2 = Brian(screen)
    scoreboard = Scoreboard()
#    enemy3 = Enemies(screen)
    back = Background()
    fore = Foreground()
    hero = Link(screen)
    
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(20)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
#                    link.loadPics()
                    hero.loadattackpics()

        goodSprites = pygame.sprite.OrderedUpdates(back, hero, fore)
        badSprites = pygame.sprite.OrderedUpdates(enemy1, enemy2)
        scoreSprite = pygame.sprite.Group(scoreboard)
# collisions
                
        hitEnemies = pygame.sprite.spritecollide(hero, badSprites, False)
        if hitEnemies:
            hero.sndThunder.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
#            for thePeter in hitEnemies:
#                thePeter.reset()
    
# Peter rolls towards Link        
        enemy1.dx -= 3
# Link moves towards Brian
        enemy2.dx -= 1
        goodSprites.update()
        badSprites.update()
        scoreboard.update()
        
        goodSprites.draw(screen)
        badSprites.draw(screen)
        scoreSprite.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
