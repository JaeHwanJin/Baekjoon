def prime_number(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, int(num ** (0.5)) + 1):
        if num % i == 0:
            return False
    return True


T = int(input())
for tc in range(T):
    num = int(input())
    while True:
        if prime_number(num):
            print(num)
            break
        else:
            num += 1