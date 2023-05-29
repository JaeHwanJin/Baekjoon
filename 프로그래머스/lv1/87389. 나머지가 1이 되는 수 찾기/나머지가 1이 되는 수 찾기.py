def solution(n):
    answer = 0
    big = []
    for i in range(1, n+1):
        if n % i == 1:
            big.append(i)
    answer = min(big)
    return answer