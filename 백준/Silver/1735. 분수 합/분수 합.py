import math
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3 = (a1 * b2) + (a2 * b1)
b3 = b1 * b2

while True:
    if math.gcd(a3, b3) == 1:
        print(a3, b3)
        break
    else:
        print(a3//math.gcd(a3, b3), b3//math.gcd(a3, b3))
        break