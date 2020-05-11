# -*- coding: utf-8 -*-
"""
Created on Mon May 11 09:49:46 2020

@author: A
"""

class calculator:
    def __init__(self):
        self.result = 0
    #인스턴스를 생성하면서 필드값을 초기화 시키는 함수        
    def add(self, num):
        self.result += num
        return self.result
    def sub(self, num):
        self.result -= num
        return self.result
    
    
cal = calculator()
#cal이라는 객체를 calculator 인스턴스로 선언,
print(cal.add(10))
print(cal.sub(2))
print(cal.result)

cal2 = calculator()

#calculator 클래스를 선언하고, add 매써드를 추가해준뒤 본문에서 클래스 객체를 선언.
#클래스내에 선언된 함수를 메써드라고 하며, 메써드 내의 self는 객채선언한 
#인스턴스 자체가 들어가게 된다. 

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
        
call = fourcal(4, 5)
call.setdata(8,4)
call.add()
call.sub()
call.mul()
call.div()

import module_class as md

call2 = md.fourcal(4,5)
call2.add()
call2.sub()
call2.mul()
call2.div()

#클래스를 모듈화 하여, 호출하는 식으로도 사용가능
#객체변수는 다른 객체들의 영향을 받지 않고 독립적으로 그 값을 유지한다. 


class morefourcal(fourcal):
    def pow(self):
       print("%d ^ %d = %d"%(self.n1, self.n2, self.n1 ** self.n2))
#클래스를 상속받는 클래스를 선언하여, 상속받은 클래스의 필드를 이용해 매써드 선언가능

a= morefourcal(4,2)
a.add()
a.sub()
a.div()
a.mul()
a.pow()


#메서드 오버라이딩->메서드 이름을 동일하게 구현하는 것을 메서드 오버라이딩이라 한다. 
#div 메써드에서 0으로 나눌수 없기 떄문에 조건을 넣어준다. 
class safefourcal(morefourcal):
      def div(self):
        if self.n1 == 0 or self.n2 == 0:
            print("0으로 나눌수 없습니다.")
        else:
            print("%d / %d = %.1f"%(self.n1, self.n2, self.n1 / self.n2))
            
a= safefourcal(4,0)
a.add()
a.sub()
a.div()
a.mul()
a.pow()

class failsafefourcal(safefourcal):
    def mul(self):
        if self.n2 ==0:
            print("Fail!")
        else:
            print("%d X %d = %d"%(self.n1, self.n2, self.n1 * self.n2 ))
            
a = failsafefourcal(4,0)
a.add()
a.sub()
a.div()
a.mul()
a.pow()
