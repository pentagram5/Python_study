# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
multiline  = "Life is too short \n you need python"
multiline

head = "python"
tail = " is fun!"

"""문자열 더하기 """
print(head + tail)
headtail = head + tail
"""문자열 곱하기 """
print(head * 2)

"""print함수의 서식"""
print("아령하세연?")
print("100")
print("%d" %100)

print("%d" % (100+100))


print("%d / %d = %f" % (100,200,0.5))

"""정수 -> %d, 실수 ->%f, 스트링 -> %s"""

"""print() 함수를 사용한 깔끔한 출력 """

print("%d" % 123)
print("%5d" % 123)
print("%05d" % 123)


print("%f" %123.45)
print("%7.f" %123.45)
print("%7.3f" %123.45)

print("%s" %"Python")
print("%10s" %"Python")

print("한행입니당. \n또다룬 한행입니당")
print("탭키 \t 탭키")
"""
\n -> 새로운 줄로 이동
\t -> 다음 탭으로 이동 
\b -> 뒤로 한칸 이동 
\\ -> \출력
\' -> ' 출력
\* -> * 출력
"""
"""문제풀어보기"""
head= "Python은"
tail=" 아주훌륭한 프로그래밍 언어이다"
line="="
print(line*50 +"\n"+head+tail+"\n"+"\b"+line *50 )

mark ="*"
i= 4
j= 1 
for x in [1,3,5,7,9]:
       print(" "*i+ mark * x)
       i =i-1
for x in [7,5,3,1]:
       print(" "*j+ mark * x)
       j =j+1  
       
       
a = 100
b = 50
result = a+b

"""input함수 활용"""
a = int(input("a를 입력하세요 :"))
b = int(input("b를 입력하세요 :"))
result = a+b
print(a,"+",b,"=",result)
result = a-b
print(a,"-",b,"=",result)
result = a*b
print(a,"*",b,"=",result)
result = a/b
print(a,"/",b,"= %.f" %result)
#%f 출력시, .3, .4와 같이 소수점 아래 몇번째까지 출력을 원하는지 정할수 있다.
"""변수는 한꺼번에 선언가능 """
x,y = 100, "김준연"
print(x,y)
type(x),type(y)
#type 함수로 변수의 타입 확인가능 
#변수명은 숫자로 시작되면 안되며, 예약어 또한 변수명으로 사용불가능하다 
#변수는 연산결과를 대입할 수도 있다.

a = 100**100
print(a)

a, b= 10, 20 
print(a+b, a-b, a*b, a/b)
print(a**b,a%b, a//b)
# %는 나머지 연산, //는 나눈 후 소수점을 버리는 연산자  **는 제곱 연산자 

a= True
type(a)

a=(100 == 200)
b= (10>100)
print(a,b)

a= "파이썬만세"
a
print(a)
type(a)

var1=input()
var2=input()
result=int(var1)*int(var2)
print(var1 , "*" , var2 , "=" , result)


a = int(input("숫자 1 입력 :"))
b = int(input("숫자 2 입력 :"))
result = a+b
print(a,"+",b,"=",result)
result = a*b
print(a,"*",b,"=",result)
result = a**b
print(a,"^",b,"=",result)


#1.아래와 같은 결과가 나오도록 프로그램 해보세요
age =int(input("당신의 나이는 몇 살이세요?"))
print("제나이는",age,"입니다.")

#2. 아래와 같은 결과가 나오도록 프로그램해보세요 
name = input("당신의 이름은?")
print("제 이름은",name,"입니다.")

#3.합쳐서 출력하기 
print("제나이는 ",age,"이고, 이름은", name,"입니다.")

#1.아래와 같은 결과가 나오도록 프로그램 해보세요
age,age2 =map(int,input("당신의 나이는 몇 살이세요?").split(','))
print("우리들의 나이는",age,",",age2,"살입니다.")
#두가지 이상의 값을 input할때, split으로 구분하여 데이터를 받는다. int형일때는
#map함수를 써줌으로서 해결된다. 

#2. 아래와 같은 결과가 나오도록 프로그램해보세요 
name,name2 = input("당신의 이름은?").split(',')
print("우리들의 이름는",name+","+name2,"입니다.")

#3.합쳐서 출력하기 
print("우리들의 나이의 합",int(age)+int(age2),"살입니다.\n그리고 이름은",name,",",name2,"입니다." )




