'''
Created on 2013-07-03
04 - inclusion of first enemy sprte
05 expectation - collision detection and enemy animation

@author: Troy
'''

import pygame, random
pygame.init()
#TRANSPARENCY = (0,0,0,0)
screen = pygame.display.set_mode((640, 480))
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
        
        self.loadPics()
        self.frame = 0
        self.delay = 3
        self.pause = self.delay
        self.dx = 4      

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

class Enemies(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy10.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (600, 375)
        self.dx = -2
        self.reset()
        
    def update(self):
        self.rect.left += self.dx
        if self.rect.left >= 0:
            self.reset() 
              
    def reset(self):
        self.rect.bottom = 375 

def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Link Running")
    
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    enemy1 = Enemies()
#    enemy2 = Enemies(screen)
#    enemy3 = Enemies(screen)
    back = Background()
    fore = Foreground()
    link = Link(screen)
    
    goodSprites = pygame.sprite.OrderedUpdates(back, link, fore)
    badSprites = pygame.sprite.Group(enemy1)
    
    
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(25)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        
        goodSprites.update()
        badSprites.update()
        goodSprites.draw(screen)
        badSprites.draw(screen)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
