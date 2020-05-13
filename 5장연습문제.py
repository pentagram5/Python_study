# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:33:24 2020

@author: A
"""

#1. calculator 클래스 

class Calculator:
    def __init__(self):
        self.value =0
    
    def add(self, val):
        self.value +=val
    
    
class upgradecCaculator(Calculator):
    def minus(self, val):
        self.value -= val
        
        
cal = upgradecCaculator()
cal.add(10)
cal.minus(7)
print(cal.value)


#2. MaxLimitCalculator 클래스 

class MaxLimitCaculator(Calculator):
        def add(self, val):
           self.value +=val
           
           if self.value > 100:
                self.value = 100
                
cal = MaxLimitCaculator()
cal.add(50)
cal.add(60)
print(cal.value)
 

# 3. 결과 예측
all([1,2,abs(-3)-3])

chr(ord('a')) =='a'


#4. filter, lambda 활용
print(list(filter(lambda x: x>0, [1,-2,3,-5,8,-3])))

#5. 10진수~16진수
int(hex(234), 16)

#6. map, lambda활용
print(list(map(lambda x: x*3, [1,2,3,4])))

#7. max,min 활용
max([-8,2,7,5,-3,5,0,1])
min([-8,2,7,5,-3,5,0,1])

#8. 반올림
print("%.4f"%(17/3))
round((17/3), 4)


#9. sys.argv활용
import sys
print(sum(map(int, sys.argv[1:])))

#10. os모듈활용
import os
os.chdir("C:/doit")
f = os.popen("dir")
print(f.read())


#11. glob 모듈활용
import glob
glob.glob("C:/doit/*.py")

#12. time 모듈활용
import time
time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))


#13. random 모듈 활용
import random
lotto_num=[]
for i in range(6):
    num=random.randint(1,45)
    if lotto_num.count(num) == 0:
        lotto_num.append(num)
    else: pass

print(lotto_num)
