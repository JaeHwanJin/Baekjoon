
def solution(n):
    answer = [0] *100001
    answer[0] = 0
    answer[1] = 1
    for i in range(2, n+1):
        answer[i] = sum(answer[i-2:i])
    return answer[n] % 1234567