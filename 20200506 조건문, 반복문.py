# -*- coding: utf-8 -*-

"""if문 활용하기"""
a = 200
a = 50
if a<100:
    print("100보다 작다 ")
else :
    print("100보다 크다 ")

print("==========결과================")
price = int(input("구입금액을 입력하시오:"))

if price > 100000:
    price = price*0.95
    print("지불 금액은 %.1f원입니다" % price)    
else :
    print("5% 할인 혜택이 없습니다.")
    print("지불금액은 %d입니다." % price)

x = 3; y =2;
x>y
x<y
x==y
x!=y

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else: 
    print("걸어가라")
    
print("=================================")
bag = float(input("짐의 무게를 입력하세요:"))
if bag >20:
    print("무거운 짐은 20,000원을 내셔야 합니다")
else:
    print("짐에 대한 수수료는 없습니다.")
print("감사합니다")


print("=================================")
tem = float(input("현재 기온를 입력하세요:"))
if tem > 30:
    print("반바지를 입으세요. ")
else:
    print("긴바지를 입으세요.")
print("나가서 운동하십쇼.")

inte = int(input("정수를 입력하세요:"))
if (inte % 2) == 0:
    print("짝수 입니다.")
else :
    print("홀수 입니다.")

#if 문에 조건부 넣어보기
#and, or, nor, in, not in etc...
money = 2000
card = input("카드가 있습니까? (y/n):")
if money >3000 or card == 'y' or card == 'Y':
    print("택시를 타고 가라")
else:
    print("걸어가세요")

x= [1,2,3]
1 in x
5 in x

'j' not in 'python'

pocket= list(input("주머니에 있는것들을 써주세요 :\n").split(','))
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가세요")


pocket2= list(input("주머니에 있는것들을 써주세요 :\n").split(','))
if 'card' or 'money' in pocket2:
    print("버스를 타시오")
else:
    print("걸어가세요")
    
pocket = ['paper','money','cellphone']
if 'money' in pocket:
    pass
else: 
    print("카드를 꺼내라")
    
    
# 중첩 if 문 사용해보기 
a = int(input("숫자를 입력해보세요:"))
if a> 50:
    if a <100:
        print("50 보다 크고, 100보다 작군요.")
    else:
        print("100보다 훨씬 크네요!")
else:
    print("50보다도 작네요!")
    
    
score = int(input("점수를 입력하세요:"))
if score >= 95:
    grade = 'A+'
elif score >= 90:
    grade = 'A'
elif score >= 85:
    grade = 'B+'    
elif score >= 80:
    grade = 'B'
elif score >= 75:
    grade = 'C+'
elif score >= 70:
    grade = 'C'
elif score >= 65:
    grade = 'D+'
elif score >=60:
    grade = 'D'
else: 
    grade = 'F'
print("학점 = %s"% grade)

    
sco = 57
if sco >= 60:
    print("합격")
elif sco >= 40:
    print("불합격이나 과락은 아님")        
else:
    print("불합격에 과락임")




while 1:
    num = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계:"))
    if num == 1:
        a = str(input("*****수식을 입력하세요 :"))
        result = eval(a)
        #eval 함수는, 사칙연산이 포함된 수식(스트링형)을 계산해주는 함수
        print(a,"의 결과는 %.1f입니다"% result)    
        break
    elif num == 2:
        a = int(input("*****첫번째 수를 입력하세요 : "))
        b = int(input("*****두번째 수를 입력하세요 : "))
        print(a,"+",b,"은 %d입니다"% (a+b))
        break
    else:
        print("1이나 2를 선택하세요")
        

mon = int(input("월을 입력하세요:"))
if mon == 2:
    print(mon,"월의 날수는 29일")
elif mon in (4,6,9,10):
    print(mon,"월의 날수는 30일")
else:
    print(mon,"월의 날수는 31일")



"""반복문while"""
num = 4
while num <1000:
    num= num+1
    print(num)
#조건문을 위반하면, while 문의 내용은 더이상 실행되지 않는다
    
i = 0
while i<10:
    print("%d : 안녕하세요? while 문을 공부중입니다. ^^7" %i)
    i = i+1
    
sum, i = 0,0
while i<11:
    sum +=i
    i = i+1
print(sum)

hap,a,b = 0,0,0

while True:
    a = int(input("1:"))
    b = int(input("2:"))
    hap = a+b
    print("%d + %d = % d"% (a,b,hap))
    
    
while True:
    one = input("첫번째 수를 입력하세요:")
    if one == '0':
        print("0이 입력되었습니다. 종료합니다.")
        break
    two = input("두번째 수를 입력하세요:")
    car = input("연산자를 입력하세요:")
    if car not in('*','/','%','+','-','**'):
        print("연산자를 잘못 입력했습니다.")
        break
    tot = one+car+two
    print("%s %s %s = %.1f" %(one, car, two, eval(tot)))
    
    
coffe = 5
while True:
    money = int(input("돈을 넣어 주세요:"))
    if money == 300:
        print("돈을 받았으니 커피를 줍니다")
        coffe -= 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." %(money -300))
        coffe -=1
    else:
        print("너한테 줄 커피는 없습니다.")
    
    print("남은 커피는 %d입니다." % coffe)
    if not coffe:
        print("재고가 없습니다. ")
        break;
    

a = 0
while a <10:
    a +=1
    if a%2 == 0:    
        continue
        #continue 아래의 코드를 실행하지 않고 while 문 처음으로 돌아간다. 
    print(a)


"""문제풀기
1. 나이는 (2020 - 태어난 연도 +1)로 계산
26세 이하 20세 이상이면 '대학생', 20세 미만 17세 이상이면 '고등학생'
17세 미만 14세 이상이면 '중학생', 14세 미만 8세 이상이면 '초등학생'
그 외의 경우는 '학생이 아닙니다.' 출력하세요.
"""
while True:
    year = int(input("당신이 태어난 년도를 입력하세요:"))
    age = 2020-year+1
    if 26>=age>=20:
        student = '대학생'
    elif 20>age>=17:
         student = '고등학생'
    elif 17>age>=14:
         student = '중학생'
    elif 14>age>=8:
         student = '초등학생'
    else:
        print("나이는 %d, 학생이 아닙니다." %age)
        continue
    print("나이는 %d, %s입니다."%(age, student))

"""
2. while문을 이용하여 아래와 같은 결과가 나오도록 프로그램을 작성해 보세요.

예- 결과1)
시작값을 입력하세요 : 2
끝값을 입력하세요 : 10
증가값을 입력하세요 : 3
2에서 10까지 3씩 증가시킨 값의 합계 : 15
"""

start = int(input("시작값을 입력하세요:"))
end = int(input("끝값을 입력하세요:"))
plus = int(input("증가값을 입력하세요:"))
i,tot = 0,0 
while (start+i) < (end+1):
    tot+=start+i
    i+=plus
print("%d부터 %d까지 %d씩 증가시킨 값의 합은 %d입니다."%(start, end, plus, tot))
    