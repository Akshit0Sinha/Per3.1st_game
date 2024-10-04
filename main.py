#this file was created by: Akshit SInha
#import all necessary modules and libraries
import pygame as pg
from settings import *
from sprites import *
from tilemap import *
from os import path
from random import randint

#create a game class to represent the examples later
# it will have all necessary parts to run the game

#Block 1
#will have all the neessary parts oto run the game and organize elements needed to create a game
#Create game class to instantiate game syste,
class Game:
    def __init__(self):
        #init initialies the screen and system below and the library of variables defined below
        pg.init()
        pg.mixer.init() #sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Akshit's Game")
        self.clock = pg.time.Clock()
        self.running = True
    
    def load_data(self):
        self.game_folder = path.dirname(__file__)
        self.map = Map(path.join(self.game_folder, 'level1.txt'))

    #Block 2 + creates a play block and defines PROPERTIES to be seen in the game system & all_sprites system
    def new(self):
        #tnks function will create everything we need to recreate objects on screen
        #create all items in terminal
        self.load_data()
        self.all_sprites = pg.sprite.Group()
        
        #self.player = Player(self, 1, 1)
        #self.mob = Mob(self, 100, 100)
        #self.wall = Wall(self, 150, 150)
        #self.wall = Wall(self, 200, 200)
        #self.wall = Wall(self, 250, 250)
        #self.player2 = Player(self, 50, 50)
        #self.all_sprites.add(self.player)
        #self.all_sprites.add(self.mob)
        #self.all_sprites.add(self.wall)
        #faster ways to write the lines of code above, shown below + makes new mobs & walls using for loops for _X_ amount of times
        #for i in range(6):
         #   Mob(self, i*randint(0,WIDTH), i*randint(0,HEIGHT))
        #for i in range(32):
         #   print(i*TILESIZE)
          #  w = Wall(self, i*TILESIZE,32)
           # self.all_sprites.add(w)
        
        for row, tiles in enumerate(self.map.data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    Player(self, col, row)
                if tile == 'M':
                    Mob(self, col, row)

       
            

        #create where mob will spawn
       # for i in range(10):
            #self.mob = Mob(randint(24,WIDTH), randint(24,HEIGHT))
            #self.all_sprites.add(self.mob)
    #block 3 + using self-running as a boolean to continue running the game
    def run(self):
        while self.running:
            #update evertyhing in sprite with four event definitions to define sprite
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
#input + Block 4 + looks for any events, and this specifically looks for closing the game with __
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
    
        #print(self.player.rect.colliderect(self.mob))
#process + Block 5 + 
    def update(self):
        self.all_sprites.update()

#output (draw) + block 6
    def draw(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        pg.display.flip()


#block 7  + CONDITIONAL statmenet that asks for a formality for coding + creates a game object
if __name__ == "__main__":
    print("main is running")
    g = Game()
    #creates all game elements with new method (not function)
    g.new()
    # run tha game
    g.run()
    print("main is running")
