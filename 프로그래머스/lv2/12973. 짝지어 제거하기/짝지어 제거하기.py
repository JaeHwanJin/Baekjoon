def solution(s):
    answer = 0
    stack = [0]
    for i in s:
        if stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()
    if len(stack) == 1:
        answer = 1            
    return answer