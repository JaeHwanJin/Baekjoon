def solution(x):
    answer = 0
    
    arr = list(str(x))
    result = 0
    for i in arr:
        result += int(i)
    if x % result == 0:
        answer = True
    else:
        answer = False
    return answer