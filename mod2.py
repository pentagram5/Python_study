#main문과, 클래스를 집어넣은 모듈
PI = 3.141592


class math:
    def solv(self, r):
        return PI *(r**2)

def add(a,b):
    return a+b

#모듈로 호출시 수행되지 않는 코드. 직접 이 파일을 컴파일시에만 main문이 수행된다. 
if __name__=="__main__":
    print(PI)
    a = math()
    print(a.solv(2))
    print(add(PI, 4.4))