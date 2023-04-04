from collections import deque

def BFS(farm, x, y):
    mr = [0, 0, 1, -1]
    mc = [1, -1, 0, 0]
    q = deque()
    q.append((x, y))
    farm[x][y] = 2  
    while q:
        x, y = q.popleft()
        for k in range(4):
            nr = mr[k] + x
            nc = mc[k] + y
            if 0 <= nr < N and 0 <= nc < M and farm[nr][nc] == 1:
                farm[nr][nc] = 2
                q.append((nr, nc))


T = int(input())

for tc in range(T):
    N, M, K = map(int, input().split())  # 배추밭의 가로, 세로, 배추가 심어져 있는 위치의 개수

    farm = [[0] * M for _ in range(N)]  # 배추밭

    cnt = 0

    for n in range(K):
        x, y = map(int, input().split())
        farm[x][y] = 1

    for x in range(N):
        for y in range(M):
            if farm[x][y] == 1:
                BFS(farm, x, y)
                cnt += 1

    print(cnt)