# -*- coding: utf-8 -*-
"""
Created on Mon May 11 09:49:46 2020

@author: A
"""

class calculator:
    def __init__(self):
        self.result = 0
        
    def add(self, num):
        self.result += num
        return self.result
    
    
cal = calculator()
print(cal.add(3))
