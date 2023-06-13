def solution(n):
    answer = list(str(n)[::-1])
    answer.sort(reverse=True)
    answer = int("".join(answer))
    
    return answer