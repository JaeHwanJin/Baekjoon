from collections import deque


def cm(i, j):
    x, y = i, j
    mr = [0, 0, 1, -1]
    mc = [1, -1, 0, 0]
    q = deque()
    q.append((i, j))
    while q:
        i, j = q.popleft()
        for k in range(4):
            nr = mr[k] + i
            nc = mc[k] + j
            if graph[x][y] == 'R':
                if 0 <= nr < N and 0 <= nc < N and mvisited[nr][nc] != 1 and graph[nr][nc] == 'R':
                    mvisited[nr][nc] = 1
                    q.append((nr, nc))
            elif graph[x][y] == 'G':
                if 0 <= nr < N and 0 <= nc < N and mvisited[nr][nc] != 1 and graph[nr][nc] == 'G':
                    mvisited[nr][nc] = 1
                    q.append((nr, nc))
            elif graph[x][y] == 'B':
                if 0 <= nr < N and 0 <= nc < N and mvisited[nr][nc] != 1 and graph[nr][nc] == 'B':
                    mvisited[nr][nc] = 1
                    q.append((nr, nc))


def cw(i, j):
    x, y = i, j
    mr = [0, 0, 1, -1]
    mc = [1, -1, 0, 0]
    q = deque()
    q.append((i, j))
    while q:
        i, j = q.popleft()
        for k in range(4):
            nr = mr[k] + i
            nc = mc[k] + j
            if graph[x][y] == 'R' or graph[x][y] == 'G':
                if 0 <= nr < N and 0 <= nc < N and wvisited[nr][nc] != 1 and (
                        graph[nr][nc] == 'R' or graph[nr][nc] == 'G'):
                    wvisited[nr][nc] = 1
                    q.append((nr, nc))
            elif graph[x][y] == 'B':
                if 0 <= nr < N and 0 <= nc < N and wvisited[nr][nc] != 1 and graph[nr][nc] == 'B':
                    wvisited[nr][nc] = 1
                    q.append((nr, nc))


N = int(input())

graph = [input() for _ in range(N)]
mvisited = [[0] * N for _ in range(N)]
wvisited = [[0] * N for _ in range(N)]

mr, wr = 0, 0
mg, wg = 0, 0
mb, wb = 0, 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R' and mvisited[i][j] == 0:
            cm(i, j)
            mr += 1
        elif graph[i][j] == 'B' and mvisited[i][j] == 0:
            cm(i, j)
            mb += 1
        elif graph[i][j] == 'G' and mvisited[i][j] == 0:
            cm(i, j)
            mg += 1

for i in range(N):
    for j in range(N):
        if (graph[i][j] == 'R' or graph[i][j] == 'G') and wvisited[i][j] == 0:
            cw(i, j)
            wr += 1
        elif graph[i][j] == 'B' and wvisited[i][j] == 0:
            cw(i, j)
            wb += 1

print(sum([mr, mg, mb]), sum([wr, wg, wb]))