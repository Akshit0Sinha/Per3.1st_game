#file created by Akshit SInha

# 1. Why is "self" needed before everything while filling image
# 2. Can we set 

import pygame as pg
from pygame.sprite import Sprite
from settings import *

class Player(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites  
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((32,32))
        self.rect = self.image.get_rect()
        self.image.fill(RED)
        #self.rect.x = x
        #self.rect.y = y
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 10
        self.vx, self.vy = 0, 0
        
    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.vy -= self.speed
        if keys[pg.K_a]:
            self.vx -= self.speed
        if keys[pg.K_s]:
            self.vy += self.speed
        if keys[pg.K_d]:
            self.vx += self.speed
    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        

        
class Mob(Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites  
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((32,32))
        self.rect = self.image.get_rect()
        self.image.fill(GREEN)
        self.rect.x = x
        self.rect.y = y
        self.speed = 10
    

    def update(self):
        #looking for key pressed, moving to side of screen
        # hit side screen, move down
        # then turns around and turns to other side of screen
        #once end of bottom right of sreen, move to top of screen
        #display  logic in the terminal
        self.rect.x += self.speed
       # self.get_keys()
       # self.x += 1

        #if self.x > WIDTH:
        if self.rect.right > WIDTH or self.rect.left < 0: 
            print("Off the screen... ")
            print(self.speed)
            print(self.rect.x)
            self.speed *= -1
            self.rect.y += 32
        elif self.rect.colliderect(self.game.player):
            self.speed *= -1
        
class Wall(Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites   
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(BLUE)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass
