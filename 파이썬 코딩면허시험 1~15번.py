# -*- coding: utf-8 -*-
"""
Created on Tue May 12 17:01:14 2020

@author: A
"""

#1. 문자열 바꾸기
def join(a,b): return a+b
txt ="a:b:c:b"
re =''
for i in list(txt.split(':')):
    re += join(i,'#')
print("%s"%re)

#2. 딕셔너리 값 추출하기
a={'A':90, 'B':80}
try:
    a['C']
except:
    a['C']=70
    print(a['C'])

#3. 리스의 더하기 와 extend 함수
    

#4. 리스트총합더하기
A = [20,55,67,82,45,33,90,87,100,25]
tot,c=0,0
for i in A:
    if i>=50: tot+=i;  c+=1
print(tot/c)

#5. 피보나치 함수
n = int(input("정수입력:"))
list_num=[]
for i in range(n):
    if i <= 1:
        list_num.append(i)
        
    else :
        if (list_num[i-1]+list_num[i-2]) < n:
            list_num.append(list_num[i-1]+list_num[i-2])
        else : break
               
print("피보나치 수열 : {}".format(list_num))


#6. 숫자의 총합 더하기 
num_list=input("숫자입력 :").split(",")
tot = 0
for i in num_list:
    tot+=int(i)
print("총합 : %d"%tot)

#7. 구구단
num = int(input("구구단을 출력할 숫자를 입력하세요(2~9):"))
for i in range(1,10):
    print("%d"%(i*num), end= ' ')


# 8. 역순저장

tt2 = open("C:\Python\\abc.txt", 'r')
lines = tt2.readlines()

tt = open("C:\Python\\abc.txt", 'w')
for i in range(4,-1,-1):
    tt.write(lines[i])

tt.close()
tt2.close()    



# 9. 평균값 구하기 
num = open("C:\Python\\sample.txt", 'r')
numbers = num.read()
num_lines =numbers.split('\n')
tot = 0
for i in num_lines:
    tot+=int(i)
data = str(tot/len(num_lines))
avg = open("C:\Python\\result.txt", 'w')
avg.write(data)
num.close()
avg.close()

# 10. 사칙연산 계산기

class Calculater(list):
    def __init__(self, list):
        self.list = list
        self.tot = 0
        
    def sum(self):
        for i in self.list:
            self.tot+=i
        return self.tot
    
    def avg(self):
        return self.tot/len(self.list)
            
cal1 = Calculater([1,2,3,4,5])
cal1.sum()
cal1.avg()

cal2 = Calculater([6,7,8,9,10])
cal2.sum()
cal2.avg()


# 11. 모듈 사용방법
# 현재의 디렉토리 경로가 mymod.py모듈과 같을경우 import 가능하며,
# 명령 프롬프트에서 PYTHONPATH를 C:\doit으로 지정하여 improt 하거나
# sys 모듈을 improt하여, sys.path 에 mymod.py 모듈의 디렉토리 경로를 추가해준다.


result =0

try:
    [1,2][3]
    "a"+1
    4 / 0
except TypeError:
    result+=1
except IndexError:
    result+=3
except ZeroDivisionError:
    result+=2
    
finally:
    result+=4
result

# 12.오류와 예외 처리
# try문의 구문상, [1,2,3][3]에서 가장먼저 IndexError가 발생하고,
#finally에서 에러 발생유무와 상관없이 코드가 실행되기 때문에 
#result 의 결과는 result=3+4 = 7이다. 


# 13. Dashinsert 함수

def dashinsert(list):
    word = ''
    for i in range(len(list)):
        word +=list[i]
        try:
            if int(list[i])%2 ==0 and int(list[i+1])%2 ==0:
               word +='*'
            
            elif int(list[i])%2 ==1 and int(list[i+1])%2 ==1 :
                word +='-'
               
        except: pass
    return word
dd=input("입력예시: ")
print("출력예시: %s"%dashinsert(dd))   

# 14. 문자열 압축하기 
final=''
text=input("입력예시 : ")
count = 1

for i in range(0,len(text)):
    try:
        if text[i] != text[i+1]:
           final+=text[i-1]+str(count)
           count = 1
       
        else: count +=1
        
    except: 
        
           final+=text[i]+str(count)
     
        
print("출력예시 : %s"%final)


# 15번 Duplicate Numbers

def Duplicate(list):
    bull_list = []

    for i in list:
        dupl = i
        test = '0123456789'
        if sorted(dupl) == sorted(test):
              bull_list.append(True)
        else :
              bull_list.append(False) 
    return bull_list

 

sadf = input("입력예시 : ")
num_list = sadf.split(' ')
print("출력 예시 : %s"%Duplicate(num_list))    
           