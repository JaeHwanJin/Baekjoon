from collections import deque


def BFS(i, j):
    mr = [0, 0, 1, -1, 1, 1, -1, -1]
    mc = [1, -1, 0, 0, 1, -1, -1, 1]
    q = deque()
    q.append((i, j))
    MAP[i][j] = 0
    while q:
        x, y = q.popleft()
        for k in range(8):
            nr = mr[k] + x
            nc = mc[k] + y
            if 0 <= nr < h and 0 <= nc < w and MAP[nr][nc]:
                MAP[nr][nc] = 0
                q.append((nr, nc))




while True:
    w, h = map(int, input().split())  # 지도의 너비와 높이
    if w == 0 and h == 0:
        break
    MAP = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if MAP[i][j] == 1:
                BFS(i, j)
                cnt += 1
    print(cnt)