from collections import deque
import sys

input = sys.stdin.readline


def BFS(q):
    mr = [0, 0, 1, -1, 0, 0]
    mc = [1, -1, 0, 0, 0, 0]
    mu = [0, 0, 0, 0, 1, -1]
    global MAX
    while q:
        k, m, n = q.popleft()
        for l in range(6):
            nr = mr[l] + m
            nc = mc[l] + n
            nu = mu[l] + k
            if 0 <= nr < M and 0 <= nc < N and 0 <= nu < K and tomato[nu][nr][nc] == 0:
                tomato[nu][nr][nc] = tomato[k][m][n] + 1
                q.append((nu, nr, nc))
                MAX = max(tomato[nu][nr][nc], MAX)
    return MAX


N, M, K = map(int, input().split())

tomato = [[list(map(int, input().split())) for _ in range(M)] for i in range(K)]

q = deque()

for k in range(K):
    for m in range(M):
        for n in range(N):
            if tomato[k][m][n] == 1:
                q.append((k, m, n))
MAX = 0
result = BFS(q)

cnt = 0
for k in range(K):
    for m in range(M):
        for n in range(N):
            if tomato[k][m][n] == 0:
                cnt += 1
if cnt >= 1:
    print(-1)
elif result == 0:
    print(0)
else:
    print(result - 1)
