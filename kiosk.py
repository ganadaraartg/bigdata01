drinks = ["아이스 아메리카노", "카페 라떼", "수박 주스", "딸기 주스"]
prices = [1500, 2500, 4000, 4200]
amounts = [0] * len(drinks)
total_price = 0

# 할인 적용 정책
DISCOUNT_THRESHOLD = 10000  # 할인이 적용되는 임계값 (임계값 이상이면 할인 적용)
DISCOUNT_RATE = 0.1  # 할인율


def apply_discount(price: int) -> float:
    if price >= DISCOUNT_THRESHOLD:
        return  price * (1 - DISCOUNT_RATE)
    return price


def get_ticket_number() -> none:
    try:
        with open("ticket.txt", "r") as fp:
            number = int(fp.read())
    except FileNotFoundError:
        number = 0

    number = number + 1

    with open("ticket.txt", "w") as fp:
        fp.write(str(number))

    print(f"번호표 : {number}")


def order_process(idx: int) -> None:
    global total_price
    print(f"{drinks[idx]}를 주문하셨습니다. 가격은 {prices[idx]}원 입니다")
    total_price = total_price + prices[idx]
    amounts[idx] = amounts[idx] + 1


def display_menu() -> str:
    print("="*30)
    menu_texts = "".join([f"{j+1}) {drinks[j]} {prices[j]}원\n" for j in range(len(drinks))])
    menu_texts = menu_texts + f"{len(drinks)+1}) 주문종료 : "
    return menu_texts


def print_receipt() -> None:
    print(f"{'상품명':^20}{'단가':^6}{'수량':^6}{'금액':^6}")
    for i in range(len(drinks)):
        if amounts[i] > 0:
            print(f"{drinks[i]:^20}{prices[i]:^6}{amounts[i]:^6}{prices[i] * amounts[i]:^6}")

    discounted_price = apply_discount(total_price)
    discount = total_price - discounted_price

    print(f"할인 전 총 주문 금액 : {total_price}원")
    if discount > 0:
        print(f"할인 금액 : {discount}원 ({DISCOUNT_RATE*100}%)")
        print(f"할인 적용 후 지불하실 총 금액은 {discounted_price}원 입니다.")
    else:
        print(f"할인이 적용되지 않았습니다.\n지불하실 총 금액은 {total_price}원 입니다.")
        print(f"현재 시각 : {now.strftime('%Y-%m-%d %H:%M:%S')}")


def test() -> None:
    pass