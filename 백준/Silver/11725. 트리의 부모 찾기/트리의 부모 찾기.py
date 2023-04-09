from collections import deque
import sys
input = sys.stdin.readline

def BFS(v):
    q = deque([v])
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visite[i] == 0:
                q.append(i)
                visite[i] = v

N = int(input())
graph = [[] * (N + 1) for _ in range(N + 1)]
visite = [0] * (N + 1)
for i in range(N - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

BFS(1)
for i in range(2, N+1):
    print(visite[i])