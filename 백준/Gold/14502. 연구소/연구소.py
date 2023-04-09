import sys
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

safe = []
virus = []
result = 0
mr = [-1, 0, 1, 0]
mc = [0, -1, 0, 1]


def BFS():
    global result
    cnt = len(safe) - 3
    q = deque([])
    for x, y in virus:
        q.append((x, y))
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            nx = xx + mr[i]
            ny = yy + mc[i]
            if 0 <= nx < N and 0 <= ny < M and GRAPH[nx][ny] == 0:
                GRAPH[nx][ny] = 2
                q.append((nx, ny))
                cnt -= 1
    result = max(result, cnt)


for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            safe.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))

for comb in combinations(safe, 3):
    GRAPH = copy.deepcopy(graph)
    for x, y in comb:
        GRAPH[x][y] = 1
    BFS()
print(result)