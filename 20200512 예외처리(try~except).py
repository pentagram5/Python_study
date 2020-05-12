
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
    
