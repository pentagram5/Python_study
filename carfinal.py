# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:49:26 2020

@author: A
"""

class car:
    color =""
    speed=0
    def __init__(self, name, speed):
        self.name = name
        self.speed=speed
        
    def getname(self):
        return self.name
    
    def getspeed(self):
        return self.speed
    
    def upspeed(self, value):
        self.speed+=value
        print("현재 속도(슈퍼클래스) : %d"%self.speed)
    def downspeed(self, value):
        self.speed-=value