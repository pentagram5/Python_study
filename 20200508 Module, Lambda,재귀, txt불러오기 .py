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



def say_myself(name,old, man= True):
    print("my age is %d"%old)
    print("my name is %s"%name)
    if man:
        print("i'm man")
    else:
        print("i'm girl")
        
    
say_myself("john", 24, False)


#txt file 불러오기 
#readline() 함수 호출시 한줄씩 읽어옴
#readlines() 함수는 모두 파일을 한번 열면 처음부터 끝까지 모든 파일의 내용을 
#읽어오는 함수 -> 한줄씩, 리스트 형태로 가져온다.
f = open("C:\Python\dream1.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
lines
f.close

#txt파일에 텍스트 추가해보기
f = open("C:\Python\new.txt", 'r')
for i in range(11,20):
    data = "%d번째 줄입니다 \n" %i
    f.write(data)
    
f = open("foo.txt",'w')
f.write("life is too short, you need python")
f.close

#with~as 객체 이름 으로 텍스트파일 생성과 동시에 문장수행 후 자동으로 close된다.
with open("foo.txt","w") as f:
    f.write("life is too short, you need python")
    
with open("C:\Python\dream1.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
        
#txt파일을 불러오고, 단어마다, 줄마다 split 하여 가져올 수 있다.        
with open("C:\Python\dream1.txt", 'r') as f:
    contents = f.read()
    #read()는 텍스트파일을 불러와서 스트링 형태로 저장하는 함수
    word_list = contents.split(" ")
    line_list = contents.split("\n")
    word_list
    line_list
    contents
