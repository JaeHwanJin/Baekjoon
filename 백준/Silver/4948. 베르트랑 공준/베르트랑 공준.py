import sys

input = sys.stdin.readline

arr = [1] * (123456 * 2 + 1)
arr[0], arr[1] = 0, 0

for i in range(2, 123456 * 2 + 1):
    if arr[i]:
        for j in range(i + i, 123456 * 2 + 1, i):
            arr[j] = 0

while True:
    N = int(input())
    if N == 0:
        break
    cnt = 0
    for i in range(N + 1, 2 * N + 1):
        if arr[i] == 1:
            cnt += 1
    print(cnt)