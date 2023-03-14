def gcd(num1, num2):  # 최대공약수를 구하는 함수
    a, b = num1, num2
    while a != 0:
        b = b % a
        a, b = b, a
    return b


N = int(input())
arr = [int(input()) for _ in range(N)]

far = list()
for i in range(len(arr) - 1):
    far.append(arr[i + 1] - arr[i])

sfar = list(set(far))
x = sfar[0]
for i in range(len(sfar) - 1):
    x = gcd(x, sfar[i + 1])
    
result = 0
for j in far:
    result += j // x - 1
print(result)