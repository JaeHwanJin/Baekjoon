from collections import deque

# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다.
N, M = map(int, input().split())

# 다음 N개의 줄에는 M개의 정수로 미로가 주어진다.
miro = [list(map(int, input())) for _ in range(N)]

mr = [-1, 0, 1, 0]  # 4방향 탐색
mc = [0, -1, 0, 1]

def BFS(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nr = mr[_] + x
            nc = mc[_] + y
            if 0 <= nr < N and 0 <= nc < M and miro[nr][nc] == 1:    # 4방향 탐색 중 이동할 수 있는 1 이라면
                q.append((nr, nc))
                miro[nr][nc] = miro[x][y] + 1
    return miro[N - 1][M - 1]


print(BFS(0, 0))