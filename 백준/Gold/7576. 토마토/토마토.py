from collections import deque


def BFS(q):
    mr = [0, 0, 1, -1]
    mc = [1, -1, 0, 0]
    MAX = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nr = mr[i] + x
            nc = mc[i] + y
            if 0 <= nr < M and 0 <= nc < N and tomato[nr][nc] == 0:
                tomato[nr][nc] += tomato[x][y] + 1
                q.append((nr, nc))
                MAX = max(MAX, tomato[nr][nc])

    return MAX


N, M = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
q = deque()

for x in range(M):
    for y in range(N):
        if tomato[x][y] == 1:
            q.append((x, y))

result = BFS(q)

cnt = 0
for i in range(M):
    for j in range(N):
        if tomato[i][j] == 0:
            cnt += 1

if cnt == 0 and result != 0:
    print(result - 1)
elif cnt == 0 and result == 0:
    print(result)
else:
    print(-1)