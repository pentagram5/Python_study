
"""for 써보기"""
for i in range(0,100,1):
    print("안녕하세요? %d번째 인사 "%(i+1))
    
    
for i in range(3):
        print("안녕하세요? %d번째 인사 "%(i+1))
#초기 값을 주어주지 않으면 자동으로 0으로 잡히고, 증가값은 1이다.
    
    
for i in range(3,0,-1):
       print("안녕하세요? %d번째 인사 "%(i))   
    
#증가값을 -로 주면 감소하게 이용할 수 있다
      
for i in range(1,6):
    print("환영합니다! %d번째 인사 "%(i))

for i in range(1,10,2):
    print("환영합니다! %d번째 인사 "%(i))
    
name = ['철수', '영희', '길동', '유신']
for i in range(0,len(name)):
    print("환영합니다! %s "%(name[i]))
      
for i in ['철수', '영희', '길동', '유신']:
    print("환영합니다! %s "%i)
#리스트와 연계해서 사용해보기   
    
for i in range(10, 1, -1):
    print(i)

    
for i in range(20, 3, -4):
    print(i)



    
for i in range(1,10,3):
    for j in range(1,10):
        print("%d * %d = %2d   %d * %2d = %2d   %2d * %2d = %d"%(i,j, i*j,
                                                            (i+1),(j),(i+1)*(j),
                                                            (i+2),(j),(i+2)*(j)))
    print("\n")
    


while True:
    num =int(input("구구단 몇단을 계산할까요?(1~9)"))
 
    if num == 99:
        print("프로그램을 종료합니다")
        break   
   
    elif num not in range(1,10,1):
        print("1과 9 사이의 수를 입력하세요")
        continue
    print("구구단 %d단을 계산합니다."%(num))
    for i in range(1,10):
        print("%d x %d = %d"%(num, i , num*i))
        #############################################################################################
"""for문을 이용해 합계 구하기"""
hap = 0
for i in range(1,11,1):
    hap+=i
print("1부터 10까지의 합계 = %d"%hap)

#############################################################################################

tot = 0
for i in range(501,1001, 2):
    tot +=i
print("501부터 1001까지 홀수의 합계 = %d"%tot)

#############################################################################################

tot = 0
for i in range(0,100, 7):
    tot +=i
print("0과 100사이의 7의 배수의 합 = %d"%tot)

#############################################################################################

tot = 0
num = int(input("숫자를 입력하세요:"))
for i in range(0,num):
    tot +=i
print("1부터 %d까지의 합계 = %d"%(num,tot))    
    
#############################################################################################
    
start = int(input("시작값을 입력하세요:"))
end = int(input("끝값을 입력하세요:"))
plus = int(input("증가값을 입력하세요:"))
tot = 0 

for i in range(start, end+1, plus):
    tot+=i
print("%d부터 %d까지의 %d만큼 증가기킨 값의 합계 = %d"%(start,end,plus,tot))    

#############################################################################################

num =int(input("구구단 몇단을 계산할까요?(1~9)"))
print("구구단 %d단을 계산합니다."%(num))
for i in range(9,0,-1):
    print("%d x %d = %d"%(num, i , num*i))

#############################################################################################

"""중첩for문 사용하기"""
for i in range(0,3):
    for k in range(0,2):
        print("파이썬은 잼민입니다. ^^ i = %d, k = %d"%(i,k))


for i in range(1,10):
    print("### %d단 ###"%i)
    for j in range(1,10):
        print("%d X %d = %2d "
              %(i,j, i*j))
    print("\n")



#############################################################################################

"""for 문에서 break사용하기"""
for i in range(1,100):
    print("for 문을 %d번 실행했습니다. " %i)
    break

hap = 0
for i in range(1,1001,2):
    hap +=i
    if hap >=1000:
        break

print("1과 1000사이의 수중, 홀수들의 합계가 1000을넘어가는 숫자= %d, 합계 = %d"%(i,hap))

#############################################################################################


"""for 문에서 continue 사용하기 """
hap ,i = 0,0

for i in range(1,101):
    if i%3 ==0:
        continue
    hap +=i
print("3의배수를 제외한 1~100까지 합계 = %d"%hap)

#############################################################################################

"""리스트와 for문 활용"""

aa=[]
for i in range(0,4):
    aa.append(0)

hap = 0
for i in range(0,4):
    aa[i] = int(input("%d번째 숫자:"%(i+1)))
    hap +=aa[i]
print("리스트 = %s, 합계 = %d"%(aa,hap))

test_list = ['one','two','three']
for i in test_list:
    print(i)
#리스트 내의 데이터를 range 개념으로 사용가능 
    
a= [(1,2),(3,4),(5,6)]
for (i,j) in a:
    print(i,j, i+j)
#튜플형태의 데이터도 출력가능하다.

marks =[90,20,50,80,77]
number =0
for score in marks:
    number = number+1
    
    if score<60: continue
    print("%d번 학생은 %d점으로, 합격입니다."%(number,score))


numlist = []
for num in range(1,6):
    numlist.append(num)
print(numlist)

#컴프리 핸션으로 줄일수 있다.->리스트 내부에 for문 사용 
#리스트 내부에 for문을 넣어주고, 변수를 range에서 정해준 범위만큼 집어넣는다. 
numlist_com = [num for num in range(1,6)]
print(numlist_com)
numlist_com = [num*num for num in range(1,6)]
print(numlist_com)
#range범위 내에서, 3의 배수인 number만 리스트에 넣어줄때 
numlist_com = [num for num in range(1,22) if num %3 ==0]
print(numlist_com)

# 다른 리스트의 value를 가져올 수도 있다. 
numlist_com2 = [num*2 for num in numlist_com if num%2 == 0]
print(numlist_com2)

#이중 for문 컴프리 핸션 구현
nine = [(str(x)+'x'+str(y)+'='+str(x*y))for x in range(2,10) for y in range(1,10)]

nine
#자주 활용되는 것이기 때문에, 잘 활용 한다.
