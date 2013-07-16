'''
Edited on 2013-07-15
sidescroller10 added instruction screen and more sounds
sidescroller11 add more enemies... this is getting annoying

@author: Troy Strachan
'''

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
        self.img = []
# link running        
        self.loadPics()
        self.frame = 0
        self.delay = 3
        self.pause = self.delay
        self.dx = 4
           
    def update(self):
        
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

class LinkAttack(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("linkattack00.png")
        self.image = self.image.convert()
        tranColor = self.image.get_at((1, 1))
        self.image.set_colorkey(tranColor)
        self.rect = self.image.get_rect()
        self.img = []
# link running        
        self.loadattackpics()
        self.frame = 0
        self.delay = 0
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
            
    def loadattackpics(self):
        for i in range(3):
            imgName = "linkattack0{0}.png".format(i)
            tmpImg = pygame.image.load(imgName)
            tmpImg.convert()
            tranColor = tmpImg.get_at((0, 0))
            tmpImg.set_colorkey(tranColor)
            self.img.append(tmpImg)       
        
class LinkDead(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("linkdead00.png")
        self.image = self.image.convert()
        tranColor = self.image.get_at((1, 1))
        self.image.set_colorkey(tranColor)
        self.rect = self.image.get_rect()
        self.img = []
        
        self.loaddeadpics()
        self.frame = 0
        self.delay = 0
        self.pause = self.delay
        self.dx = -2      

    def update(self):
        self.rect.center = (320, 375)
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
        self.dx = 2
        self.reset()
        #controls when to loop the background
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right <= 620:
            self.reset() 
    
    def reset(self):
        self.rect.bottom = screen.get_height()            
        self.rect.left = 0
        print "new background"

# scrolling foreground        
class Foreground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("hedgeslong.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        #controls the speed of the movement - moves slightly faster than background
        self.dx = 3
        self.reset()
        
    def update(self):
        self.rect.centerx -= self.dx
        if self.rect.right <= 620:
            self.reset() 
    
    def reset(self):
        self.rect.bottom = screen.get_height()            
        self.rect.left = 0
        print "new foreground"
#enemy 1
class Peter(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy010.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.img = []
        #initialize animated sprites
        self.loadPics()
        self.frame = 0
        self.delay = 3
        self.pause = self.delay
         
        self.reset()   
        
# Peter rolling towards Link
    def update(self):
        self.rect.center = (640, 375)
        self.pause -= 1
        if self.pause <= 0:
            self.pause = self.delay
        # incease frame to loop images - appearance of animation
        self.frame += 1
        if self.frame > 4:
            self.frame = 0
        #dig up images from array 
        self.image = self.img[self.frame]
        # takes center of the image to create the illusion of animation, replaces image on previous image center
        self.rect.centerx += self.dx
        if self.rect.centerx > self.screen.get_width():
            self.rect.centerx = 0
        #allows the enemy to move to the left. IF ">" is replaced with "<" image just loops on itself and stays in place
        if self.rect.left > screen.get_width():
            self.reset()
                
    def loadPics(self):
        # looping through the array of pngs
        for i in range(5):
            imgName = "enemy01{0}.png".format(i)
            tmpImg = pygame.image.load(imgName)
            tmpImg.convert()
            tranColor = tmpImg.get_at((0, 0))
            tmpImg.set_colorkey(tranColor)
            self.img.append(tmpImg)
            
    def reset(self):
        self.rect.bottom = screen.get_height()            
        self.rect.left = 0
        self.dx = random.randint(2,15)
        print "new Peter"

#enemy 2           
class Brian(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy010.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.img = []
        #initialize animated sprites
        self.loadPics()
        self.frame = 0
        self.delay = 3
        self.pause = self.delay
        self.dx = 0
        self.reset() 

    def update(self):
        #starting point of the character (x,y)
        self.rect.center = (640, 375)
        self.pause -= 1
        if self.pause <= 0:
            self.pause = self.delay
        # incease frame to loop images - appearance of animation
        self.frame += 1
        if self.frame > 4:
            self.frame = 0
        #dig up images from array 
        self.image = self.img[self.frame]
        # takes center of the image to create the illusion of animation, replaces image on previous image center
        self.rect.centerx += self.dx
        if self.rect.centerx > self.screen.get_width():
            self.rect.centerx = 0
        #allows the enemy to move to the left. IF ">" is replaced with "<" image just loops on itself and stays in place
        if self.rect.left > screen.get_width():
            self.reset()
                
    def loadPics(self):
        for i in range(5):
            imgName = "enemy02{0}.png".format(i)
            tmpImg = pygame.image.load(imgName)
            tmpImg.convert()
            tranColor = tmpImg.get_at((0, 0))
            tmpImg.set_colorkey(tranColor)
            self.img.append(tmpImg)
            
    def reset(self):
        self.rect.bottom = screen.get_height()
        self.rect.left = 0
        print "New Brian"
        
class Scoreboard(pygame.sprite.Sprite):
    #scoreboard tracking with lives and score. default lives = 3 default score = 0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 3
        self.score = 0
        self.font = pygame.font.SysFont("None", 30)
        #updates the score
    def update(self):
        self.text = "Lives: %d                                                                      score: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (0, 0, 255))
        self.rect = self.image.get_rect()

def instructions(score):
    pygame.display.set_caption("Link versus Family Guy")

    
    insFont = pygame.font.SysFont(None, 50)
    insLabels = []
    instructions = (
    "          Link versus Family Guy.",
    "                   Last score: %d" % score ,
    "Instructions:  Link has fallen into",
    "the twilight zone and he must get",
    "out, but first he must defeat a", 
    "cartoon family.",
    "",
    "Press space bar to attack.",
    "Each enemy is worth different",
    "number of points",    
    "",
    "Good luck Link you will need it!",
    "",
    "click to start, escape to quit..."
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 255, 0))
        insLabels.append(tempLabel)
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
          
    pygame.mouse.set_visible(True)
    return donePlaying

def game():
    
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Link Vs Family Guy")
    
    background = pygame.Surface(screen.get_size())
    screen.blit(background, (0, 0))
    
    if not pygame.mixer:
        print("problem with sound")
    else:
        pygame.mixer.init()
        sndBgMusic = pygame.mixer.Sound("LOZ - final.ogg")
        sndHitPeter = pygame.mixer.Sound("petergriffinlaugh.ogg")
        sndBrianKilled = pygame.mixer.Sound("Brian.ogg")
        sndSword = pygame.mixer.Sound("swordswing.ogg")
        sndPeterKilled = pygame.mixer.Sound("peter.ogg")
        sndLinkDead =  pygame.mixer.Sound("LinkDead.ogg")
        sndBgMusic.play(-1)
    
    sndBgMusic.play()
    scoreboard = Scoreboard()

    back = Background()
    fore = Foreground()
    hero = Link(screen)
    heroAttack = LinkAttack(screen)
    heroDead = LinkDead(screen)
    enemy1 = Peter(screen)
    enemy2 = Brian(screen)
    
    Sprites = pygame.sprite.OrderedUpdates(back, hero, enemy1, enemy2 , fore)
    badSprite1 = pygame.sprite.Group(enemy1)
    badSprite2 = pygame.sprite.Group(enemy2)
    scoreSprite = pygame.sprite.Group(scoreboard)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        #controls the speed of the game
        clock.tick(25)
        
        pygame.mouse.set_visible(False)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    hero.remove(Sprites)
                    heroAttack.add(Sprites)
                    Sprites = pygame.sprite.OrderedUpdates(back, heroAttack, enemy1, enemy2 , fore)
                    sndSword.play()

            elif event.type == pygame.KEYUP:
                heroAttack.remove(Sprites)
                hero.add(Sprites)
                Sprites = pygame.sprite.OrderedUpdates(back, hero, enemy1, enemy2 , fore)

# collisions            
        hitByPeter = pygame.sprite.spritecollide(hero, badSprite1, True)
        hitByBrian = pygame.sprite.spritecollide(hero, badSprite2, True)
        attackPeter = pygame.sprite.spritecollide(heroAttack, badSprite1, True)
        attackBrian = pygame.sprite.spritecollide(heroAttack, badSprite2, True)
        
        if hitByPeter:
            sndHitPeter.play()
            scoreboard.lives -= 3
#new enemy of the same kind is spawned after previous is destroyed
            Peter(screen)
        if hitByBrian:
            scoreboard.lives -= 3
#new enemy of the same kind is spawned after previous is destroyed
            Brian(screen)
#When attacking Link hits enemies points are awarded and enemies are removed
        if attackPeter:
            scoreboard.score += 10
            sndPeterKilled.play()
            enemy1.remove(Sprites)
            
        if attackBrian:
            scoreboard.score += 5
            sndBrianKilled.play()
            enemy2.remove(Sprites)
# when player dies screen slows down and player spins
        if scoreboard.lives <= 0:
            hero.remove(Sprites)
            enemy1.kill()
            enemy2.kill()
            clock.tick(20)
            sndBgMusic.stop()
            sndLinkDead.play()
            heroDead.add(Sprites)
            pygame.display.set_caption("GAME OVER!")
            
# increases speed of images after you hit a certain score
        if scoreboard.score == 15:
            enemy1.dx -= 1
            enemy2.dx -= 1
            
        if scoreboard.score == 25:
            enemy1.dx -= 2
            enemy2.dx -= 2
            
# Peter rolls towards Link at random speeds
        enemy1.dx -= random.randint(1,15)
# Link moves towards Brian at 2 different speeds
        enemy2.dx -= random.randint(1,2)
        
        Sprites.update()
        badSprite1.update()
        badSprite2.update()
        scoreboard.update()
        
        Sprites.draw(screen)
        badSprite1.draw(screen)
        badSprite2.draw(screen)
        scoreSprite.draw(screen)

        pygame.display.flip()

def main():
    donePlaying = False
    score = 0
    while not donePlaying:
        donePlaying = instructions(score)
        if not donePlaying:
            score = game()
            
if __name__ == "__main__":
    main()
