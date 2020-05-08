# -*- coding: utf-8 -*-


def coffee(num):
    if num == 1:
        print("보통커피를 준비한다")
    elif num == 2:
        print("설탕커피를 준비한다.")
    elif num == 3:
        print("블랙커피를 준비한다.")
    elif num == 4:
        print("아무커피를 준비한다.")        
        
coffee(num= int(input("번호를 쓰시오(1~4):")))


def plus(v1, v2):
    result = 0
    result = v1+v2
    return result

hap = 0

hap = plus(100,200)
print("100과 200의 plus() 함수의 결과 %d"%hap)


def calcurate(v1,v2, op):
    tot=0
    tot = str(v1)+op+str(v2)
    return eval(tot)

while True:
    op = input("연산자를 입력해주세요(0 입력시 종료):")
    if op == '0':
        print("종료합니다.")
        break 
    elif op not in ('+','-','/','*','**','%','^'):
        print("정확한 연산자를 입력해주세요.")
        continue
    
    v1=int(input("첫번째 수를 입력하세요:"))
    
    v2=int(input("두번째 수를 입력하세요:"))
    if op == '/' and v2 == 0:
        print("0으로 나눌 수 없습니다. 다시입력해주세요")
        continue
    
    result = calcurate(v1,v2, op)
    print("%d %s %d = %.1f 입니다"%(v1,op,v2,result))


def func1():
    a= 10
    print("func1 a값 %d"%a)
    
def func2():
    print("func2 a값 %d"%a)
    
a = 20
func1()
func2()
    
#지역변수 - 지정된 클래스나 함수내에서만 통용되는 변수
#main문이나, 연동되는 모든 라인에서 통용되는 변수


def multi(v1,v2):
    retlist = []
    res1 = v1+v2
    res2 = v1-v2
    retlist.append(res1)
    retlist.append(res2)
    return retlist

mylist = []
hap, sub = 0,0
mylist = multi(200,100)
hap = mylist[0]
sub  = mylist[1]
print(hap,sub)

def hap(haplist):
    tot = 0
    for i in haplist:
        tot+=i
    
    return tot 

print(hap(av))


av=[1,2,4]
def para_func(*para):
    result = 0
    for num in para:
        result += num
    
    return result

print(para_func(av[0],av[1],av[2]))

#딕셔너리 형태의 매개변수를 키= 값으로 사용할 수 있다.
def dic_func(**para):
    for k in para.keys():
        print("%s --> %d명입니다. " %(k, para[k]))

dic_func(트와이스 =9, 소녀시대 = 7, 걸스데이 =4, 블랙핑크 =4)


"""문제풀어보기""""
#두수를 곱하는 함수
def multi2(v1,v2):
    return v1*v2

a = multi2(200,88)
print(a)

#입력받은 수중 가장 큰 값을 출력하는 함수 
def maxnum(*para):
    max =0
    for num in para:
        if max < num:
           max = num
     
    return max

a = maxnum(1,23,4,2351,34,135)
print(a)

#random 패키지 생성 후 난수 생성 -> 로또로 사용해보기 
import random

def getnumber():
    return random.randrange(1,46)
    #난수 발생 범위를 지정해준다. 
lotto=[]
num =0

while len(lotto) < 7:
    num = getnumber()
    if lotto.count(num) ==0:
        lotto.append(num)
   
lotto.sort()
print("당첨번호는 %s입니다!"%(lotto))

