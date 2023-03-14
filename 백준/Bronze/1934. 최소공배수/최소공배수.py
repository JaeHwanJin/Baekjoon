import sys
def gcd(num1, num2): # 최대 공약수를 구하는 함수
    a, b = num1, num2
    while True: # 유클리드 호제법 활용
        b = b % a
        a, b = b, a
        if a == 0:
            return b

for n in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    print(a * b // gcd(a, b))   # 정수론에 의하면 a * b = 최대공약수 * 최소공배수