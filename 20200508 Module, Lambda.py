# -*- coding: utf-8 -*-

"""module1 호출"""
import module1 as md
md.func1()
md.func2()
md.func3()
md.func4()
md.func5()

import sys
print(sys.builtin_module_names)


"""lambda 활용"""
hap2 = lambda num1,num2:num1+num2
print(hap2(10,20))
#lambda 매개변수 : 수식 으로, 함수화를 간단히 만들 수 있다. 

hap3 = lambda num1 = 10, num2=20:num1+num2
print(hap3())
print(hap3(300,400))
#초기 매개변수에 값자체를 넣어줄 수도있고, 람다함수를 호출하면서 값을 넣어줄수도있다.

mylist = [1,2,3,4,5]
add10 = lambda num : num+10

mylist = list(map(add10, mylist))
mylist

#lambda를 활용해 리스트에 값을 매칭할 수도 있다. 

mylist = list(map(lambda num : num +10, mylist))
mylist
#매핑에서 직접 lambda를 활용할 수도 있다.

"""재귀함수"""
#자신이 자신을 호출하는 함수 
def selfcall():
    print('하', end = '')
    selfcall()
selfcall()

#지정한 수부터 1까지 세는 함수 
def count(num):
    if num >=1:
        print(num, end = ' ')
        count(num-1)
    else:
        return
count(10)
count(10**3)

#지정한 수부터 팩토리얼 값을 구하는 함수 
def fac(num):
    if num >1:
        return num * fac(num-1)   
    else:
        return num

fac(4)


def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum

mysumli=[23,12434,135433513,445436,56456,547]

sum_many(2,3,5,43,3)