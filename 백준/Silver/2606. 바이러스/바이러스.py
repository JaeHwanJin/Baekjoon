from collections import deque
def BFS(v, cnt):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        for i in range(node + 1):
            if graph[v][i] and not visited[i]:
                q.append(i)
                visited[i] = 1
                cnt += 1
                # print(visited)
    return sum(visited) - 1

node = int(input())
branch = int(input())
graph = [[0] * (node + 1) for _ in range(node + 1)]
visited = [0] * (node + 1)
cnt = 0
for i in range(branch):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
cnt = 0
# print(graph)
print(BFS(1, cnt))