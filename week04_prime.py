def is_prime(number):
    if number >= 2:
        i=2
        while i * i <= number:
            if number % i == 0:
                return False
            print(i, end=" ")
            i=i+1
        else:
            return False
        return True

    n = int(input())
    if is_prime(n):
        print(f"{n}는(은) 소수 입니다.")
    else:
        print(f"{n}는(은) 소수가 아닙니다!")