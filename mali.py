import numpy as np

import random, sys

import pgzrun

class Brick(Actor):

    def react(self):

        if np.abs(mario.center[1]+mario.size[1]/2-self.center[1]+self.size[1]/2)<15: # z gory

            mario.vy = 0

            mario.bottom = self.top

        elif np.abs(mario.center[1]-mario.size[1]/2-self.center[1]-self.size[1]/2)<15: # z dolu

            mario.vy = 0

            mario.top = self.bottom

        elif np.abs(mario.center[0]+mario.size[0]/2-self.center[0]+self.size[0]/2)<15: # z prawej

            moveall(6)

        elif np.abs(mario.center[0]-mario.size[0]/2-self.center[0]-self.size[0]/2)<15: # z lewej

            moveall(-6)

    def move(self):

        pass

 

class Coin(Actor):

    def react(self):

        if mario.colliderect(self):

            #sounds.coin.play()

            objs.remove(self)

            mario.points=mario.points+1

    def move(self):

        pass

 

class Block(Actor):

    def react(self):

        if np.abs(mario.center[1]+mario.size[1]/2-self.center[1]+self.size[1]/2)<15: # z gory

            mario.vy = 0

            mario.bottom = self.top

        elif np.abs(mario.center[1]-mario.size[1]/2-self.center[1]-self.size[1]/2)<15: # z dolu

            mario.vy = 0

            mario.top = self.bottom

            animate(self, pos=(self.center[0], -10000))

        elif np.abs(mario.center[0]+mario.size[0]/2-self.center[0]+self.size[0]/2)<15: # z prawej

            moveall(6)

        elif np.abs(mario.center[0]-mario.size[0]/2-self.center[0]-self.size[0]/2)<15: # z lewej

            moveall(-6)

    def move(self):

        pass

 

class Mushroom(Actor):

    def react(self):

        if self.colliderect(mario):

            mario.small=False

            objs.remove(self)

    def move(self):

        for obj in objs:

            if obj!=self and self.colliderect(obj) and not obj.image in ["bush.png","brick.png","hill.png"]:

                self.dir=-self.dir

 

        self.x=self.x+self.dir

 

        uy=self.vy

        self.vy=self.vy+2000.0*0.015

        self.y=self.y+(uy+self.vy)*0.5*0.015

 
