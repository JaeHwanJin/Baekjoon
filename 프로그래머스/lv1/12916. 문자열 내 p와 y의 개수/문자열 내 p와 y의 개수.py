def solution(s):
    answer = True
    s = list(map(str, s))
    if 'p' not in s and 'y' not in s:
        return True
    else:
        P = s.count('p') + s.count('P')
        Y = s.count('y') + s.count('Y')
        if P == Y:
            answer = True
        else:
            answer = False
    return answer

