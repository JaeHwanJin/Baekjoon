from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())  # 정점의 개수 N, 간선의 개수 M
graph = [[0] * (N + 1) for _ in range(N + 1)]  # 각 정점에 연결된 다른 점들

for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [0] * (N + 1)  # 이미 방문한 점


def BFS(v):
    if visited[v] == 0:
        q = deque()
        q.append(v)
        visited[v] = 1
        while q:
            v = q.popleft()
            for i in range(1, N + 1):
                if graph[v][i] == 1 and not visited[i]:
                    q.append(i)
                    visited[i] = 1


cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        BFS(i)
        cnt += 1

print(cnt)