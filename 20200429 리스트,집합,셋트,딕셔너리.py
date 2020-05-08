# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:39:01 2020

@author: A
"""

a = [1,'a','b','c',4]
a[1:3] = []
a
#리스트 a의 1번 주소부터 3번까지 []로 대체 하겠다. 

del a[0]
#특정 주소만 삭제 

a = [1,2,3]
a.append(4)
a
#a리스트마지막 순서에 요소 추가 

a.sort()
#리스트 정렬 

a.reverse()
#리스트 뒤집기 
a.index(4)
#특정 요소의 위치를 반환 index

a.pop()
#가장 마지막 요소를 출력하고, 그요소는 삭제되는 함수 

a.count(2)
#리스트 a안에, 특정요소의 갯수를 출력해주는 함수

a.extend([6,5])
#리스트 a를 확장 : extend([,,])

b = [7,8]
a.extend(b)
#리스트를 확장 함수의 변수로도 사용할 수 있다.

a,b,c,d = 0,0,0,0

total = 0

a = int(input("1번째 숫자 : "))
b = int(input("2번째 숫자 : "))
c = int(input("3번째 숫자 : "))
d = int(input("4번째 숫자 : "))

total = a+b+c+d
print("합계 ==> %d 입니다" %total)

"""리스트활용"""
aa = [10,20,30,40]

aa = [0,0,0,0]
hap = 0

for i in range(0,4):
    aa[i] = int(input("%d번째 숫자:" %(i+1)))
    total += aa[i]
print("합계 ==> %d 입니다" %total)
#input을 위해선, 원하는 요소의 갯수만큼 리스트가 초기화되어야 한다. 

aaa =[]
aaa.append(0)
aaa.append(0)
aaa.append(0)
aaa.append(0)
print(aaa)

aaa =[]
for i in range(0,10000):
    aaa.append(0)
len(aaa)
print(aaa)



"""튜플 자료형 """
t1 = (1,2,'a','b')
del t1(0)
#리스트는 그 값의 생성 삭제 수정이 가능하지만 튜플은 값을 바꿀수는 없다. 

t1[0]
#인덱싱 가능
t1[1:]
#슬라이싱 가능

t2 = (3,4)
t1+t2
#튜플끼리 요소를 한번에 출력할수있다 :+연산자
t2*3
#튜플의 요소를 곱셈연산으로 중복출력할수 이따
tt1 =(10,20,30)
tt2 = 10,20,30
#튜플의 생성에서 소괄호는 생략이 가능하다. 읽기만 가능한 자료 저장시 사용

tt3 = (10)
tt4 = 10
tt5 =(10,)
tt6= 10,
#자료형을 생성할때, 튜플로 사용하고 싶다면 요소들 사이사이 , 기호를 넣어줘야한다. 

del(tt1)
#튜플 그자체는 삭제가 가능함

mytu = (10,20,30)
myli = list(mytu)
myli.append(40)
mytu = tuple(myli)
mytu
#튜플의 값을 수정하기 위해선 리스트로 형변환후, 수정하고 다시 튜플로 형변환해준다.


"""딕셔너리 자료형"""
#key를 통해 value를 얻는 사전적 자료형, 해시라고 볼수 있다.
dic ={'name':'pey', 'phone':'011993323', 'birth':'1118'}
#요소는 key:value 형태로 저장된다. 

a = {1:'a'}
a[2] = 'b'
dic['sex'] = 'man'
del a[1]
del dic['name']
#딕셔너리의 요소 삽입 및 삭제 

dic['sex']
#딕셔너리 생성시, key가 중복되지 않도록 유의하자

#key리스트 만들기 
dic.keys()
#key값만 출력해준다.
dic.values()
#value값만 출력해준다. 
dic.items()
#key와 value 쌍으로 출력하기 

student = {'학번':1000, '이름':'홍길동','학과':'컴퓨터학과'}
student['핸드폰'] = '123-456-789'
student['이름']
student.get('이름')

'이름' in student
#딕셔너리내에 키 조사 

####문제풀기

mylist = [30,10,20]
mylist.append(40);mylist
mylist.pop();mylist

mylist.sort();mylist
mylist.reverse();mylist
mylist.index(20)
mylist.insert(2,222);mylist
mylist.remove(222);mylist
mylist.extend([77,88,77]);mylist
mylist.count(77)


"""집합자료형 -집합에 관련된 것을 쉽게 처리하기위한 자료형으로, 
중복과 순서가 없다."""

s1 = set([1,2,3])
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
s1&s2
s1.intersection(s2)
#교집합 연산자로, 두 집합 자료형에서 겹치는 요소를 출력해준다.

s1|s2
s1.union(s2)
#두집합의 합집합 연산자로,겹치는 요소는 한번만 출력해준다. 

s1-s2
s2-s1
s1.difference(s2)
#두집합의 차집합 연산자, 

s1 ^ s2
#대칭 차집합으로,두 집합 사이에서 중복된 데이터를 뺀 나머지 요소 출력 


s1.add(7)
s1
#집합에 값 추가하기

s1.update([8,9]) 
#집합에 여러값 추가하기

s1.remove(9)
#집합에서 특정값 삭제하기 

myset1 = {1,2,3,3,3,4}
myset1
salelist = {'김밥','라면','김밥','아이스크림', '음료수'}
salelist
#중괄호로도 세트생성이 가능하다. 중복된 형태는 제거되서 저장됨
#키만 모아놓은 딕셔너리의 특수한 형태로도 셋트는 사용가능하다.
