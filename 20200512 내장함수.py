# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:43:46 2020

@author: A
"""
"""파이썬 내장함수"""
#절대값 반환 함
abs(-3)
abs(-1.2)


#요소가 모두 참일때 true, 하나라도 0일떄 false를 반환하는 all 함수
all({1,3,3,})


#요소가 하나라도 참이면 true를 반환하는 any
any({0,0})
any({0,1})


#아스키코드값에 매칭되는 문자형으로 리턴해주는 함수
chr(88)
chr(97)


#자료형에 따라 사용할 수 있는 함수,리스트 반환, 구조형도 반환해주는 함수
dir({1,2,3})
dir({'1':'a'})


#몫과 나머지를 리턴해주는 함수
divmod(7,3)
divmod(1.3,0.2)


#for문처럼 반복되는 구간에서, 객체의 현재 위치를 알려주는 인덱스값이 필요할떄 사용
#특정 리스트에 i,name in enumerate(리스트)로 사용하면된다.
for i, name in enumerate(['body','foo','bar']):
    print(i, name)
    

#실행 가능한 문자열을 입력으로 받아, 문자열을 실행한 결과를 리턴해주는 함수
eval('1+2')
eval("'go'+' to the blue'")
eval('divmod(4,3)')


#filter -> 원하는 함수를 호출하여, 특정리스트나 라인들을 함수에 걸쳐 반환되는 값만
#필터링 해주는 함수
def positive(x):
    return x>0
print(list(filter(positive, [1,-3,0,-5,6])))

print(list(filter(lambda x: x>0, [1,2,5,-2,3])))


#정수값을 입력받아 16진수로 변환하여 리턴해주는 함수
hex(234)
hex(1235471349)


#id-> 객체를 입력받아 객체의 고유 주소값(레퍼런스)를 리턴하는 함수이다.
a=3
id(3)
id(a)
b=a
id(b)

#int
int('1a', 16)
int('743', 8)

#isinstance 특정 객체가 특정 클래스의 인스턴스인지 확인하는 기능
class person:pass
a = person()
isinstance(a,person)

