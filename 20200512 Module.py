#main문을 집어넣어, 모듈 호출시 필요하지 않는 문장 제어
import mod1
print(mod1.add(3,5))

from mod1 import add

add(3,4)

from mod1 import *

add(3,5)
sub(2,3)

#main문과 class를 선언하여 사용해보기 
import mod2 
print(mod2.PI)
a = mod2.math()
print(a.solv(2))
print(mod2.add(mod2.PI, 4.4))

#파이썬이 설치된 path 확인 하기위한 라이브러리 모듈 호출-> sys모듈
import sys
sys.path
#sys.path 추가하기 
sys.path.append("C:\doit")
sys.path.append("C:\Users\A\Anaconda3\DataScience")
