# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:01:38 2020

@author: A
"""

def coffee(num):
    if num == 1:
        print("보통커피를 준비한다")
    elif num == 2:
        print("설탕커피를 준비한다.")
    elif num == 3:
        print("블랙커피를 준비한다.")
    elif num == 4:
        print("아무커피를 준비한다.")        
        
coffee(num= int(input("번호를 쓰시오(1~4):")))