N = int(input())
square = [[0] * 1002 for _ in range(1002)]  # 색종이가 놓일 평면크기
num = 1
for n in range(N):
    x, y, l, h = map(int, input().split())
    for i in range(x, x + l):   # 색종이마다 저장 될 수를 다르게 해서 보이는 부분 표시
        for j in range(y, y + h):
            square[i][j] = num
    num += 1

num = 1
result = []

for n in range(N):
    cnt = 0
    for k in range(len(square)):
        for l in range(len(square)):
            if square[k][l] == num:
                cnt += 1
    result.append(cnt)
    num += 1
    print(result[n])