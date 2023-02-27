# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지
paper = [[0] * 100 for _ in range(100)]

# 첫째 줄에 색종이의 수가 주어진다.
# 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다.
# 색종이를 붙인 위치는 두 개의 자연수로 주어지는데 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고,
# 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다.

N = int(input())
cnt = 0

for n in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] += 1
            if paper[i][j] == 1:
                cnt += 1
print(cnt)