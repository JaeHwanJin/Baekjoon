while True:
    a, b, c = map(int, input().split())
    arr = [a, b, c]
    if a == b == c == 0:
        break
    if max(arr) >= sum(arr) - max(arr):
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a == b or b == c or a == c:
        print('Isosceles')
    else:
        print('Scalene')