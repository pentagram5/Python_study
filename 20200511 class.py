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



#클래스 변수

class Family:
    lastname = "김"
    
print(Family.lastname)#직접 클래스의 변수를 불러올 수 있고,
a = Family()# a객체를 생성한뒤에 변수이름을 직접호출할 수도 있다.
a.lastname
Family.lastname = "박"
a.lastname
#클래스외부에서 변수내용 변경가능


#자동차 클래스 만들어보기
class car:
    color =""
    speed=0
    def upspeed(self, value):
        self.speed+=value
        
    def downspeed(self, value):
        self.speed-=value
        
mycar1= car()
mycar2= car()
mycar3= car()
     
mycar1.color = "빨강"
mycar2.color = "파랑"
mycar3.color = "노랑"  

mycar1.upspeed(30)
mycar2.upspeed(60)
print("자동차 1의 색상은 %s이며, 현재 속도는 %dkm입니다."%(mycar1.color, mycar1.speed))
print("자동차 2의 색상은 %s이며, 현재 속도는 %dkm입니다."%(mycar2.color, mycar2.speed))
print("자동차 3의 색상은 %s이며, 현재 속도는 %dkm입니다."%(mycar3.color, mycar3.speed))

#모듈화 하여 호출하고, 속도가 150 이상일 경우 속도 고정하기 
import code12 as car_code

mycar1 = car_code.car()
mycar2 = car_code.car()
mycar3 = car_code.car()
mycar1.color = "빨강"
mycar2.color = "파랑"
mycar3.color = "노랑"  
mycar1.upspeed(30)
mycar2.upspeed(60)
mycar3.upspeed(200)
print("자동차 1의 색상은 %s이며, 현재 속도는 %dkm입니다."%(mycar1.color, mycar1.speed))
print("자동차 2의 색상은 %s이며, 현재 속도는 %dkm입니다."%(mycar2.color, mycar2.speed))
print("자동차 3의 색상은 %s이며, 현재 속도는 %dkm입니다."%(mycar3.color, mycar3.speed))