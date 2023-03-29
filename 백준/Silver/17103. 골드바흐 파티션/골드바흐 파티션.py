import sys

input = sys.stdin.readline

arr = [1] * 1000001
arr[0], arr[1] = 0, 0
for i in range(2, int(1000001 ** (0.5)) + 1):
    if arr[i] == 1:
        for j in range(i+i, 1000001, i):
            arr[j] = 0

T = int(input())

for tc in range(T):
    N = int(input())
    cnt = 0
    for k in range((N // 2) + 1):
        if arr[k] and arr[N - k]:
            cnt += 1
    print(cnt)