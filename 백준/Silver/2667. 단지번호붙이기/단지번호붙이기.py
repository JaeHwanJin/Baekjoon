from collections import deque

def BFS(x, y):
    mr = [0, 0, 1, -1]
    mc = [1, -1, 0, 0]
    q = deque()
    q.append((x, y))
    home[x][y] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nr = mr[i] + x
            nc = mc[i] + y
            if 0 <= nr < N and 0 <= nc < N and home[nr][nc] == 1:
                cnt += 1
                home[nr][nc] = 0
                q.append((nr, nc))
    return cnt


N = int(input())
home = [list(map(int, input())) for _ in range(N)]

result = []
for i in range(N):
    for j in range(N):
        if home[i][j] == 1:
            result.append(BFS(i, j))

result.sort()
print(len(result))
for k in result:
    print(k)