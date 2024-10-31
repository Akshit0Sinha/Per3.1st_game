#file created by Akshit SInha

# 1. Why is "self" needed before everything while filling image
# 2. Can we set 

import pygame as pg
from pygame.sprite import Sprite
from settings import *
from main import *

import random

vec = pg.math.Vector2


class Player(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites  
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((32,32))
        self.rect = self.image.get_rect()
        self.image.fill(RED)
        self.rect.x = x
        self.rect.y = y
        # self.pos.x = pos.x * TILESIZE
        # self.y = y * TILESIZE
        self.pos = vec(x*TILESIZE, y*TILESIZE)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.speed = 5
        self.jumping = False
        self.jump_power = 25
       # self.vx, self.vy = 0, 0
        self.coins = 0
        self.vx, self.vy = 0, 0


    
        
    def get_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.vy -= self.speed
        if keys[pg.K_a]:
            self.vel.x -= self.speed
        if keys[pg.K_s]:
            self.vy += self.speed
        if keys[pg.K_d]:
            self.vel.x += self.speed
        if keys[pg.K_SPACE]:
            self.jump()
        
    def jump(self):
        print("I'm trying to jump")
        print(self.vel.y)
        self.rect.y += 2
        hits = pg.sprite.spritecollide(self,self.game.all_walls, False)
        self.rect.y -= 2
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -self.jump_power

        
    #modify player dynamics by adding blockers to player movement
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                    self.vel.x = 0
                    self.rect.x = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self,self.game.all_walls, False)
            if hits:
                if self.vel.y > 0:
                    self.y = hits[0].rect.top - TILESIZE
                    self.jumping = False
                if self.vel.y < 0:
                    self.x = hits[0].rect.bottom
                    self.vel.y = 0
                    self.rect.y = self.pos.y
                    

    def collide_with_stuff(self, group, kill):
        hits = pg.sprite.spritecollide(self, group, kill)
        if hits:
            if str(hits[0].__class__.__name__) == "Powerup":
                print("I hit a powerup")
                self.speed += 5
        if hits:
            if str(hits[0].__class__.__name__) == "Coin":
                print("I hit a powerup")
                self.coins += 1

    def update(self):
        self.acc = vec(0, GRAVITY)
        self.get_keys()
        self.acc.x += self.vel.x * FRICTION
        self.vel += self.acc

        if abs(self.vel.x) < 0.1:
            self.vel.x = 0

        self.collide_with_stuff(self.game.all_powerups, True)
        self.collide_with_stuff(self.game.all_coins, True)

        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        
        self.rect.y = self.pos.y
        self.collide_with_walls('y')
        

        
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
      #  self.rect.pos.x += self.speed
       # self.get_keys()
       # self.pos.x += 1

        #if self.pos.x > WIDTH:
        if self.rect.right > WIDTH or self.rect.left < 0: 
            print("Off the screen... ")
            print(self.speed)
            print(self.rect.x)
            self.speed *= -1
            self.rect.y += 32
        #elif self.rect.colliderect(self.game.player):
          #  self.speed *= -1
        
        
        
        
class Wall(Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.all_walls 
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(BLUE)
        self.rect.x = x*TILESIZE
        self.rect.y = y * TILESIZE

    def update(self):
        pass

class Coin(Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.all_coins
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(YELLOW)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Powerup(Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.all_powerups
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(GREEN)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE




        #self.pos += self.vel + 0.5 * self.acc

        # self.y += self.vy * self.game.dt
        # self.y += self.vy