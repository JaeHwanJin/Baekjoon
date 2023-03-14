def L(n1, n2):
    a, b = n1, n2
    while True:
        if a == 0 :
            return b
        else:
            b = b % a
            a, b = b, a

num1, num2 = map(int, input().split())
print(num1 * num2 // L(num1, num2))