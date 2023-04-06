from collections import deque


def BFS(a, b):
    mr = [2, 2, -2, -2, 1, 1, -1, -1]
    mc = [1, -1, 1, -1, 2, -2, 2, -2]
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for k in range(8):
            nr = mr[k] + x
            nc = mc[k] + y
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                visited[nr][nc] = visited[x][y] + 1
                q.append((nr, nc))


T = int(input())

for tc in range(T):
    N = int(input())  # 체스판 크기
    chess = [[0] * N for _ in range(N)]  # 체스판
    visited = [[0] * N for _ in range(N)]
    x1, y1 = map(int, input().split())  # 체스말의 현재 위치
    x2, y2 = map(int, input().split())  # 체스말이 이동하려는 위치
    BFS(x1, y1)
    if x1 == x2 and y1 == y2:
        print(0)
    else:
        print(visited[x2][y2])