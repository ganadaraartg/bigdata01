drinks = ["아이스 아메리카노", "카페 라떼", "수박 주스", "딸기 주스"]
prices = [1500, 2500, 4000, 4200]

total_price = 0
amounts = [0] * len(drinks)

def order_process(idx : int) -> None:
    """
    주문 처리 함수 1) 주문 디스플레이  2) 총 주문 금액 누산  3) 주문 품목 수량 업데이트
    :param idx: 고객이 선택한 메뉴 - 1 (인덱스, 정수)
    :return: 없음
    """
    global total_price
    print(f"{drinks[idx]}를 주문하셨습니다. 가격은 {prices[idx]}원 입니다")
    total_price = total_price + prices[idx]
    amounts[idx] = amounts[idx] + 1


def display_menu() -> str:
    print("="*30)
    menu_texts = "".join([f"{j+1}) {drinks[j]} {prices[j]}원\n" for j in range(len(drinks))])
    menu_texts = menu_texts + f"{len(drinks)+1}) 주문종료 : "
    return menu_texts

try:
    while True:
        menu = 0
        menu = int(input(display_menu()))
        if len(drinks) >= menu >= 1:
            order_process(menu - 1)
        elif menu == len(drinks)+1:
            print("주문을 종료합니다")
            break
        else:
            print(f"{menu}번 메뉴는 존재하지 않습니다. 아래 메뉴에서 골라주세요")
except ValueError:
    print(f"{menu}는 잘못된 입력입니다. 숫자를 입력해주세요.")

print(f"{'상품명':^20}{'단가':^6}{'수량':^6}{'금액':^6}")
for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]:^20}{prices[i]:^6}{amounts[i]:^6}{prices[i] * amounts[i]:^6}")

print(f"총 주문 금액 : {total_price}원")