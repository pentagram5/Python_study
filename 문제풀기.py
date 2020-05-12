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

