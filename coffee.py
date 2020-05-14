coffee = 5
while True:
    money = int(input("돈을 넣어 주세요:"))
    if money == 300:
        print("%d원을 받았으니 커피를 줍니다" % money)
        coffee -= 1
    elif money > 300:
        print("거스름돈 %d원를 주고 커피를 줍니다." %(money -300))
        coffee -=1
    else:
        print("돈이 부족합니다.")
    
    print("남은 커피는 %d잔 입니다.\n" % coffee)
    
    if not coffee:
        print("재고가 없습니다. ")
        break;
