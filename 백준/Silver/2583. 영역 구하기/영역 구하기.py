from pprint import pprint
import sys
sys.setrecursionlimit(100000) #없으면 recursion error 발생
M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            graph[j][k] = 1

# pprint(graph)
# pprint(visited)

def DFS(st, end):
    mr = [0, 0, 1, -1]
    mc = [1, -1, 0, 0]
    visited[st][end] = 1
    global cnt
    for k in range(4):
        nr = mr[k] + st
        nc = mc[k] + end
        if 0 <= nr < M and 0 <= nc < N and graph[nr][nc] == 0 and visited[nr][nc] == 0:
            cnt += 1
            graph[nr][nc] = 1
            DFS(nr, nc)


cnt = 1
area = 0
result = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            area += 1
            DFS(i, j)
            result.append(cnt)
            cnt = 1
print(area)
print(*sorted(result))