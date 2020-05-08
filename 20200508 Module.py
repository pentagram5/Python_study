# -*- coding: utf-8 -*-

import module1 as md
md.func1()
md.func2()
md.func3()
md.func4()
md.func5()

import sys
print(sys.builtin_module_names)

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