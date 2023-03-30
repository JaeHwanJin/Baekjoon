T = int(input())
arr = [25, 10, 5, 1]
for t in range(T):
    N = int(input())
    for i in arr:
        a = N // i
        N = N % i
        print(a, end=' ')