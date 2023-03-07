arr = [list(map(int, input().split())) for _ in range(9)]
MAX = 0
x, y = 0, 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > MAX:
            MAX = arr[i][j]  # 행열에 있는 값마다 비교해서 큰 값을 MAX로
            x, y = i, j
print(MAX)
print(x + 1, y + 1)  # list는 0부터 시작하기때문에