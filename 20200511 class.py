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



#클래스 선언부에서 생성자 선언해주기 
class car:
    color =""
    speed=0
    def __init__(self):
        self.color = "빨강"
        self.speed = 0
    def upspeed(self, value):
        self.speed+=value
        
    def downspeed(self, value):
        self.speed-=value
        
        
        
#매개변수가 있는 생성자로 선언
        
class car:
    def __init__(self, va1, va2):
        self.color = va1
        self.speed = va2
        
mycar1 = car("빨강", 200)
print(mycar1.color,mycar1.speed)


#car_final
import carfinal as car

car1 = car.car("아우디", 0)
car2 = car.car("벤츠", 30)
print(car1.getname(), car1.getspeed())
print(car2.getname(), car2.getspeed())


#인스턴스 변수와 클래스 변수는, 변수처리가 외부에서 이뤄지는지, 클래스 내부에서
#이뤄지는지 확인해야한다.
class car :
    color=""
    speed = 0
    count = 0
      
    def __init__(self, name, speed):
        self.name = name
        self.speed=speed
        car.count +=1
        
    def upspeed(self, value):
        self.speed+=value
        print("%s --> 현재 속도(슈퍼클래스) : %dkm, 전체 차량수 = %d"%(self.name, self.speed, car.count))
           
    def downspeed(self, value):
        self.speed-=value
        

#슈퍼클래스 car->  세단 클래스 오버라이딩
class sedan(car):
    def upspeed(self, value):
        self.speed+=value
        
        if self.speed >= 150:
            self.speed = 150
            print("%s --> 현재 속도(서브클래스) : %dkm, 전체 차량수 = %d"% (self.name, self.speed, car.count))

#서브클래스 sedan-> 소나타 클래스 오버라이팅 
class sonata(sedan):
    pass


#슈퍼클래스 car-> 트럭클래스 오버라이딩
class cartruck(car):
    tons = 0
    def tonecheck(self):
        print("%s의 화물 무게 = %.1f"%(self.name, self.tons)) 
        #클래스 호출한 객체에서 변수조정이 이뤄지기 떄문에 인스턴스 변수이다. 
        

truck1 = cartruck("트럭", 200)
truck1.tons = 1.5
truck1.tonecheck()
sedan1 = sedan("승용차", 150)
sonata1 = sonata("소나타", 150)
truck1.upspeed(0)
sedan1.upspeed(300)
sonata1.upspeed(100)
#세단과 소나타 클래스는 속도제한 조건문을 넣어주었다. 


"""문제풀기"""
#1번

class car:
    color = ""
    speed = 0
    
    def upSpeed(self, value):
        self.speed += value
        
    def downSpeed(self, value):
        self.speed -=value
        
#2번

class car:
    color = ""
    speed = 0

myCar1= car()
myCar1.color ="빨강"
myCar1.speed = 30
print("자동차 1의 색상은 %s이며, 현재 속도는 %dkm 입니다."%(myCar1.color, myCar1.speed))


#3번

class Car:
    speed = 0
    def __init__():
        Car.speed = 50
        
        

#4번
        
class car:
    speed = 0
    
    def upSpeed(self, value):
        self.speed = self.speed+ value
        
        
class RVcar(car):
    seatNum = 0
    
    def getseatnum(self):
        return self.seatNum