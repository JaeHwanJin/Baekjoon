def change(n):
    num = []
    while n > 0:
        x = n % 2
        n //= 2
        num.append(str(x))
    num = "".join(reversed(num))
    result = num.count('1')
    return result

def solution(n):
    answer = change(n)
    print(answer)
    result = 0
    for i in range(n+1, 1000001):
        if answer == change(i):
            return i        
    # return result
    