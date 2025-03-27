def is_prime(number):

    if number < 2:
        for i in range(2, number ** 0.5 + 1):
            if number % i == 0:
                return False
    else:
        return False
    return True


    n = int(input())
    if is_prime(n):
        print(f"{n}는(은) 소수 입니다.")
    else:
        print(f"{n}는(은) 소수가 아닙니다!")