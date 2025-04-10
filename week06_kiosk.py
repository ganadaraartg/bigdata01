drinks = ["아이스 아메리카노", "카페라떼"]
prices = [2000,2500]
total_price = 0
while True:
    menu = input(f"1) {drinks[0]} {prices[0]} 2) {drinks[1]} {prices[1]} 3) 주문 종료 : ")
    if menu == "1":
        print(f"{drinks[0]}를 주문하셨습니다. 가격은 {prices[0]}원 입니다.")
        total_price = total_price + prices[0]
    elif menu == "2":
        print(f"{drinks[1]}를 주문하셨습니다. 가격은 {prices[1]}원 입니다.")
        total_price = total_price + prices[1]
    elif menu == "3":
        print("주문 종료.")
        break
    else:
        print(f"{menu}번 메뉴는 존재하지 않습니다.")

print(f"총 주문 금액 : {total_price} 원.")