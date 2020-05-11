# -*- coding: utf-8 -*-
"""
Created on Mon May 11 13:56:19 2020

@author: A
"""

class car:
    color =""
    speed=0
    def upspeed(self, value):
        self.speed+=value
        if self.speed >= 150:
            self.speed = 150
        
    def downspeed(self, value):
        self.speed-=value
        