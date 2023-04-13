N = int(input())
a, b = map(int, input().split())  # 촌수를 계산해야 하는 서로 다른 사람
M = int(input())  # 부모 자식들 간의 관계의 개수
graph = [[] for _ in range(N + 1)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [0] * (N + 1)

cnt = 0
result = []

def DFS(start, end):
    global cnt
    visited[start] = 1
    cnt += 1
    if start == end:
        result.append(cnt)
    for i in graph[start]:
        if not visited[i]:
            DFS(i, end)
            cnt -= 1


DFS(a, b)

if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)