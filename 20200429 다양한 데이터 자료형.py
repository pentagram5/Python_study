# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:39:01 2020

@author: A
"""

a = 5 ; b = 3
print(a+b, a-b,a*b,a/b,a%b,a**b)

#산술 연산자의 우선순위 - 곱셉,나눗셈 - 덧셈,뺄셈 순서(수학), 왼쪽에서 오른쪽순서,()사용하면 우선순위
a,b,c = 2,3,4
print(a+b-c, a+b*c, a*b/c)

#산술 연산을 하는 문자열과 숫자의 상호 변환
#문자열이 숫자로 구성되어있을떄, int() 또는 float() 함수 사용해서 정수나 실수로 변환
#문자열을 int() 함수가 정수로, float()함수가 실수로 변경
s1,s2,s3 = "100","100.123","9999999999999999999999999999999999"
print(int(s1)+1, float(s2)+1,int(s3)+1)
#" "사용하여 문자로 인식 되기때문에 int(), float() 함수 사용하여 연산

#숫자를 문자열로 변환하려면 str()함수 사용
#a,b가 문자열로 변경되어 100+1이 아닌 문자열의 연결인 '1001'과'100.1231'이 됨
a = 100 ; b = 100.123
print(str(a) + '1') ; print(str(b) + '1')
#print()함수는 출력 결과에 작은따옴표가 없어 문자열인지 구분하기가 어려워 사용하지않음

#산술연산자와 대입연산자
#대입연산자 = 외에도 +=,-=,*=,/=,//=,**= 사용
# 예) 첫번째 대입연산자 a+=3은 a에 3을 더해서 다시 a에 넣으라는 의미로 a=a+3과 같음
#파이썬에는 c/c++, 자바 등의 언어에 있는 증가 연산자 ++나 감소연산자--가 없음
a=10
a+=5;print(a)
a-=5;print(a)
a*=5;print(a)
a/=5;print(a)
a//=5;print(a)
a%=5;print(a)
a**=5;print(a)

##변수선언
money, c500 = 0,0
##메인코드
money = int(input("얼마를 교환하시겠습니까?:"))
c500 = money //500
money %= 500
c100 = money //100
money %= 100
c50 = money //50
money %= 50
c10 = money //10
money %= 10

print("\n 500원짜리 ==>  %d개" %c500)
print("\n 100원짜리 ==>  %d개" %c100)
print("\n 50원짜리  ==>  %d개" %c50)
print("\n 10원짜리  ==>  %d개" %c10)
print("\n 바꾸지 못한 잔돈 ===>  %d원" %money)

c50000, c10000,c5000,c1000 = 0,0,0,0
money = int(input("얼마를 교환하시겠습니까?:"))
c50000 = money //50000
money %= 50000
c10000 = money //10000
money %= 10000
c5000 = money //5000
money %= 5000
c1000 = money //1000
money %= 1000

print("\n 50000원짜리 ==>  %d장" %c50000)
print("\n 10000원짜리 ==>  %d장" %c10000)
print("\n 5000원짜리  ==>  %d장" %c5000)
print("\n 1000원짜리  ==>  %d장" %c1000)
print("\n 바꾸지 못한 잔돈 ===>  %d원" %money)

#관계연산자의 개념
#어떤것이 크거나 작거나 같은지 비교하는것(참은True, 거짓은 False로 표시)
#주로 조건문(if), 반복문(while)에 많이 사용
a,b = 100, 200
print(a==b, a!=b, a>b, a<b, a>=b, a<=b)
#a 와 b를 비교하는 관계연산자 ==를 사용하려다 착오로 =을 하나만 쓴 코드
#빨간색 오류로 나타남. a=b는 b값을 a에 대입하라는 의미임.

######문자열 자료형
#인덱싱(Indexing)
a = "Life is too short, You need python"
a[0]
a[12]
a[19]
a[-1]
#   파이썬은 0부터 숫자를 센다.
a[-0]
a[-2]
a[-5]
#  - 표시는 뒤부터 시작, 0은 상관없음.
b = a[0] + a[1] + a[2] + a[3]
b
# 슬라이싱(Slicing)
a = "Life is too short, You need python"
a[0:4]
a[0:5]
a[12:17]
# 데이터분석 자료정제시 사용 - ex)서울시데이터, 서울특별시 데이터등 변수명 정제시
a[19:]   # :뒤에 지정하지않으면 끝까지 지정.
a[:7]    # :앞에 지정하지 않으면 처음부터 지정.
a[:]    # : 둘다 지정 하지 않으면 전체 지정.
a[19:-7]    #반대로 지정가능

a = "20010331Rainy"
date = a[:8]
weather = a[8:]
date
weather
year = a[:4]
year
day = a[4:8]
day
# 슬라이싱 - Piton을 Python으로 바꾸려면
a = "Pithon"
a[1]
a[1] = "y"
a
a[:1]
a[2:]
a[:1] + 'y' + a[2:]

#홍길동씨의 주민등록번호는 881120-1068234이다. 홍길동씨의 주민등록번호를 연월일(YYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해보자.
pin = "881120-1068234"
yymmdd = pin[:6]
yymmdd
num = pin[-7:]
num
print(yymmdd)
print(num)

# string = "orajava"일때 아래와 같은 결과가 나오도록 출력해보세요.
string = "orajava"
print(string)
print(string[3:8])
print(string[:3])
print(string[:4])
print(string)

#문자열 포매팅
#숫자 바로 대입
"I eat %d apples." %3
#문자열 바로 대입
"I eat %s apples." %"five"
#숫자값을 나타내는 변수로 대입
number = 3
"I eat %d apples." %number

number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." %(number,day)
# 순서대로 같은갯수 변수를 지정해줘야함. ex) %d, %s == number, day (day,number)안됨.

#정렬과 공백
"%10s" %"hi"
# 전체 길이가 10개인 문자열 공간에서 hi를 오른쪽으로 정렬
"%-10s" %"hi"
# 왼쪽으로 정렬

#소수점표현
"%0.4f" %3.42134234
"%10.4f" %3.42134234

#문자열 개수 세기(count)
a = "hobby"
a.count('b')

#위치알려주기1(find)
a = "Python is best choice"
a.find('b')
a.find('k')    #찾는문자나 문자열이 존재하지 않는다면 -1을 반환

#위치알려주기2(index)
a = "Life is too short"
a.index('t')
a.index('k')

#문자열삽입(join)
a = ","
a.join('abcd')

#소문자를 대문자로 바꾸기(upper)
a = "hi"
a.upper()

#대문자를 소문자로 바꾸기(lower)
a = "HI"
a.lower()

#양쪽 공백 지우기(strip) - 왼쪽공백 lstrip, 오른쪽공백 rstrip
a = " hi "
a.strip()

#문자열 바꾸기(replace)
a = "Life is too short"
a.replace("Life","Your Leg")

#문자열 나누기(split)
a = "Life is too short"
a.split()    # 공백을 기준으로 문자열을 나눔.
a = "a:b:c:d"
a.split(':')    # :기호를 기준으로 문자열을 나눔.

#리스트자료형
#1,3,5,7,9 라는 숫자 모음
odd = [1,3,5,7,9]
odd
#리스트명 = [요소1,요소2,요소3.....]
#c/c++나 자바 같은 프로그래밍 언어에는 리스트가 없음, 리스트와 비슷한 개념인 배열(Array)을 사용. 리스트는 정수, 문자열, 실수 등 서로 다른 데이터형도 하나로 묶을 수 있지만, 배열은 동일한 데이터형만 묶을수있다. 정수 배열은 정수로만 묶어서 사용. 파이썬이 자유로움.

a = []    #공백의 리스트
b = [1,2,3]    #숫자만 포함된 리스트
c = ['Life','is','too','short']    #문자만 포함된 리스트
d = [1,2,'Life','is']    #숫자와 문자가 포함된 리스트
e = [1,2,['Life','is']]    #숫자와 리스트가 포함된 리스트

#리스트의 인덱싱
a = [1,2,3]
a[0]
a[0] + a[2]
a[0],a[2]
a[-1]


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
s1.symmetric_difference(s2)
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

a= [1,2,3,4]
while a:
    print(a.pop())
    
#a의 리스트가 빌때, false 값을 가지므로 while 반복문이 종료됨

"""문제풀어보기-"""
colors = ['red','blue','green']
print("1) %s" %colors[0],"\n2) %s" %colors[2], 
    "\n3) %d ==> 리스트길이를 출력" % len(colors))

string = "python1"
string[3:]
string[0:3]
string[0:4]
string[0:]


color1=colors
color2 = ['orange', 'black','white']

color1+color2
color1*2
color1+color2[0:2]

mylist=[[1,2,3,4], [5,6,7,8], [9,10,11,12]]
mylist[0][1]
mylist[1][3]
mylist[2]

test = [ '설현' , '초아' , '지민', '유나' , '유경', '혜정' , '민아', '찬미' ]
test[0]
test[6]
test[0:1]
test[6:8]
test[1:3]
test[1::3]
