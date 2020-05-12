
"""예외처리""" 
#try 내부의 문장을 수행하는 도중, except에 주어진 조건에 해당하는 예외가 발생하면
#except 문을 수행하도록 한다.
try:
    for i in range(4,-1,-1):
        print(4/i)
        
except ZeroDivisionError as e:
    print(e)


try:
    for i in range(4,-1, -1):
        print(4/i)
        
except ZeroDivisionError :
    print("에러입니다")



#숫자를 입력받아 원의 둘레, 넓이를 구한다. 정수가 아니면 error 코드를 출력한다.
# type 1--> if~else문
PI = 3.14
    
radi = input("정수입력 : ")
if radi.isdigit():
    #입력받은 변수가 숫자인지 판별하는 함수 
    radi = int(radi)
    print("원의 반지름 :",radi)
    print("원의 둘레: ",(2*PI*radi))
    print("원의 넓이: ", PI *(radi**2))
else:
    print("정수가 아닌 다른값이 들어왔습니다. ")    

# type 2--> try, except문 -> 변수형변환의 필요성이 줄고, 간단
while True:
    try:
        PI = 3.14
        radi = int(input("정수입력 : "))
        print("원의 반지름 :%d"%radi)
        print("원의 둘레: %.2f"%(2*PI*radi))
        print("원의 넓이: %.2f"%( PI *(radi**2)))
        break
    except ValueError as e:
        print("정수가 아닌 다른값이 들어왔습니다. 다시입력하세요\n에러내용:",e)
        continue
    
    
# type 3 --> try, except, else -> 에러가 발생할 코드 다음에 except문을 넣어주고,
# 에러가 발생하지 않는다면 else문을 수행하도록 -> 가시성좋으나 코드가 길어진다. 
        
while True:
    try:
        PI = 3.14
        radi = int(input("정수입력 : "))
    
    except ValueError as e:
        print("정수가 아닌 다른값이 들어왔습니다. 다시입력하세요\n에러내용:",e)
        print(str(e))
        continue

    else:
        print("원의 반지름 :%d"%radi)
        print("원의 둘레: %.2f"%(2*PI*radi))
        print("원의 넓이: %.2f"%( PI *(radi**2)))
        break 
    


#try ~finally 문
#finally 절은 트라이문 수행도중 예외 발생 여부에 상관없이 항상 수행된다.
        

try:
    f = open('foo.txt', 'w')
    
except FileNotFoundError as e:
    print(e)
    
finally: 
    f.close()
    #예외 발생 여부에 상관없이 항상 수행되어야한다. 
    
    
#여러개의 오류 처리하기 
try:
    a = [1,2]
    print(a[3])
    4/0
    
except ZeroDivisionError as e: 
    print("0으로 나눌 수 없습니다.")
    print(e)
    
except IndexError as e:
    print("인덱싱 할수 없습니다.")    
    print(e)
    
#오류 회피하기 
try:
    f=open("없는파일",'r')
except FileNotFoundError:
    pass
    
    
    
#예외 강제로 발생하기
class bird:
    def fly(self):
        raise NotImplementedError
        #raise 예외 객체 

a = bird()
a.fly()


#try~except~else~finally~
try:
    PI = 3.14
    radi = int(input("정수입력 : "))
    
except ValueError as e:
    print("정수가 아닌 다른값이 들어왔습니다. 다시입력하세요\n에러내용:",e)
       
else:
    print("원의 반지름 :%d"%radi)
    print("원의 둘레: %.2f"%(2*PI*radi))
    print("원의 넓이: %.2f"%( PI *(radi**2)))
    print("예외발생되지 않음")
finally:
    print("finally 문 실행됩니다./프로그램 종료")
        
        
#문제풀어보기
# 1번
list_number = [12,773,42,172,100]
while True:
    try:
        num = int(input("정수입력 :"))
        print("%d번째 요소 : %d"%(num, list_number[num]))
    except IndexError:
        print("인덱스를 벗어났어요")
    
    except ValueError:
        print("정수를 입력해주세요")
    
# 2번
# 방법 1
lista =["2","소나기","32","장마","125","77"]
list_digit = []
for i in lista:
    try:
        list_digit.append(str(int(i)))
    except ValueError:
        pass


print("%s 중에 숫자만 고르면 \n%s입니다."%(lista,list_digit))
print("{} 중에 숫자만 고르면".format(lista))
print("{} 입니다.".format(list_digit))
        
# 방법 2        
lista =["2","소나기","32","장마","125","77"]
print("{} 중에 숫자만 고르면".format(lista))
for i in lista:
    try:
        int(i)
    except ValueError:
        lista.remove(i)
        
print("{}입니다.".format(lista))

