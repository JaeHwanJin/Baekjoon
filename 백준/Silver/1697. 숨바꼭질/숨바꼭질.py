from collections import deque

N, K = map(int, input().split())
MAX = 100001
visited = [0] * MAX


def BFS(N):
    q = deque()
    q.append(N)
    visited[N] = 0
    while q:
        N = q.popleft()
        if N == K:
            return visited[N]
        for num in (N - 1, N + 1, N * 2):
            if 0 <= num < MAX and visited[num] == 0:
                visited[num] = visited[N] + 1
                q.append(num)
print(BFS(N))