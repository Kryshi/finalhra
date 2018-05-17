#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17th 2018 13:00-ish

@author: KrySt
"""
from math import sin, cos, radians, pi
from random import randint

import pyglet
window = pyglet.window.Window() #okno aplikace
batch = pyglet.graphics.Batch() #drawy thingy 
seznam = list()


class Ship(object):
    def __init__(self, obrazek, x = None, y = None, r = None,
                             window=window, batch=batch, rychlost = 10):
        self.image = pyglet.image.load("bigship.png")
        self.image.anchor_x = self.image.width //2
        self.image.anchor_y = self.image.height //2
        self.sprite = pyglet.sprite.Sprite(self.image, batch=batch)
        
        
        if self._x = window.width:
            self._rotation = 
            self._rotation = self.sprite.rotation
            
        
        if x:
            self._x= x
        else:
            self._x= randint(0, window.width)
        self.sprite.x = self._x
        if y:
            self._y= self.sprite.y = y
        else:
            self._y= randint(0, window.height)
        self.sprite.y = self._y
        if r:
            self._rotation = r
        else:
            self._rotation = randint(0,360)
        self.sprite.rotation = self._rotation
        
        self._rychlost = rychlost
        seznam.append(self)
    
    def tick(self, t):
        self.sprite.x = self.sprite.x + self._rychlost * t * sin ( pi * self._rotation/180)
        self._x = self.sprite.x
        self.sprite.y = self.sprite.y + self._rychlost * t * cos ( pi * self._rotation/180)
        self._y = self.sprite.y
        
        
            
@window.event
def on_draw():
    window.clear()
    batch.draw()



Falcon = Ship("bigship.png", rychlost = 75)
Enterprise = Ship("bigship.png", rychlost = 50)
Dwarf = Ship("bigship.png", rychlost = 100)


def tick(t):
    for Ship in seznam:
        Ship.tick(t)
    #Dwarf.tick(t)
    #Enterprise.tick(t)
    #Falcon.tick(t)

print("Dwarf:", Dwarf._x, Dwarf._y)
print("Enterprise:" ,Enterprise._x, Enterprise._y)
print("Falcon:", Falcon._x, Falcon._y)


pyglet.clock.schedule_interval(tick, 1/25)
pyglet.app.run()