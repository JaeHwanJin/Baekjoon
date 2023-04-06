from collections import deque


def BFS(x, y):
    mr = [0, 0, 1, -1]
    mc = [1, -1, 0, 0]
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nr = mr[k] + x
            nc = mc[k] + y
            if 0 <= nr < N and 0 <= nc < N and island[nr][nc] > H and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append((nr, nc))


N = int(input())

island = [list(map(int, input().split())) for _ in range(N)]

MAX = max(max(*island))

H = 0
M = 0
while H < MAX:
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if island[i][j] > H and visited[i][j] == 0:
                BFS(i, j)
                cnt += 1
    M = max(M, cnt)
    H += 1
    # print('i : ', island)
    # print('v : ', visited)
print(M)
