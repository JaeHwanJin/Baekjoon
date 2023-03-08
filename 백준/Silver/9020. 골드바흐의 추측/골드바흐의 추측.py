# 소수인지 확인하는 함수
def prime(n):
    if n == 1:
        return False
    # n이 n제곱은 이하의 수로 나누어 떨어지지 않으면 그 이상의 수로도 나누어 떨어지지 않는다.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


T = int(input())
for tc in range(T):
    num = int(input())
    pn1, pn2 = num // 2, num // 2   # num을 반으로 나누고 각 각 +1 -1 해주면서 두 수가 소수인지 확인
    while pn1 > 0:
        if prime(pn1) and prime(pn2):
            print(pn1, pn2)
            break
        else:
            pn1 -= 1
            pn2 += 1