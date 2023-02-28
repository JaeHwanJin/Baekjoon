arr = [[0] * 102 for _ in range(102)]  # 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지

N = int(input())  # 색종이의 수
cnt = 0
mr = [0, 0, 1, -1]
mc = [1, -1, 0, 0]
for tc in range(N):
    x, y = map(int, input().split())  # 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리, 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리
    # 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이
    for i in range(y+1, y + 11):
        for j in range(x+1, x + 11):
            if 0 < i < 101 and 0 < j < 101:
                arr[i][j] = 1
for k in range(1, 101):
    for l in range(1, 101):
        for h in range(4):
            nr = k + mr[h]
            nc = l + mc[h]
            if 0 <= nr < 102 and 0 <= nc < 102 and arr[k][l] == 1 and arr[nr][nc] == 0:
                cnt += 1
print(cnt)

# 가로변, 세로변의 길이를 구할 때 서로 값이 다르면으로 비교 가능