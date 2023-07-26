def solution(n):
    answer = 1
    start = 1
    while True:
        SUM = 0
        for i in range(start, n):
            SUM += i
            if SUM == n:
                answer += 1
                break
            if SUM > n:
                break
        start += 1
        if start >= n:
            break
    return answer


