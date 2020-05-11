# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:24:05 2020

@author: A
"""

class fourcal:
    def __init__(self, num1, num2):
        self.result = 0
        self.n1 = num1
        self.n2 = num2
     
    def setdata(self, num1, num2):
        self.n1 = num1
        self.n2 = num2
        print(self.n1, self.n2)
        
    def add(self):
        print("%d + %d = %d"%(self.n1, self.n2,self.n1 + self.n2))
        
    def sub(self):
        print("%d - %d = %d"%(self.n1, self.n2, self.n1 - self.n2))
        
    def mul(self):
        print("%d X %d = %d"%(self.n1, self.n2, self.n1 * self.n2 ))
        
    def div(self):
        print("%d / %d = %.1f"%(self.n1, self.n2, self.n1 / self.n2))