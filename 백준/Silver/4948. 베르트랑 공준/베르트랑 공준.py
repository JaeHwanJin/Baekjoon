import sys

input = sys.stdin.readline


def prime_number(num):
    for i in range(2, int(num ** (0.5)) + 1):
        if num % i == 0:
            return 0
            break
    else:
        return 1


while True:
    N = int(input())
    if N == 0:
        break
    cnt = 0
    for i in range(N + 1, 2 * N + 1):
        if prime_number(i) == 1:
            cnt += 1
    print(cnt)