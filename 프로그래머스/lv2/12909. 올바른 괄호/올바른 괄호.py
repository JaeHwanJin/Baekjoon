def solution(s):
    answer = []
    for i in s:
        if i == '(':
            answer.append(i)
        else:
            if answer:
                answer.pop()
            else:
                return False
        
    if len(answer) == 0 :
        return True
    else:
        return False
    