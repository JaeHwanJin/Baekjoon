while True:
    N = int(input())
    if N == -1:
        break
    divisor = []
    for i in range(1, N + 1):
        if N % i == 0:  # N으로 나눴을 때 몫이 0 이면 약수
            divisor.append(i)
    if sum(divisor) - N == N:   # N을 제외한 약수들의 합이 N이면 완전수
        divisor.pop(-1)
        print(N, '= ', end='')
        print(*divisor, sep=' + ')
    else:
        print(f'{N} is NOT perfect.', end='')
        print()