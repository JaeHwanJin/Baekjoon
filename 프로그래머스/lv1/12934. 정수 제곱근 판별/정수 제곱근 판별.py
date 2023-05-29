import math
def solution(n):
    answer = math.sqrt(n)
    if answer == int(answer):
        answer = (answer+1)**2
    else:
        answer = -1
        
    return answer
    
    