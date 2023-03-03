H, W = map(int, input().split())
District = [list(map(str, input())) for _ in range(H)]

for i in range(H):
    move = 1
    meet = 0  # 구름을 만날때 안만날때 구분하기 위한 변수
    for j in range(W):
        if District[i][j] == 'c' and meet == 0:
            District[i][j] = 0
            meet = 1
            move = 1
        elif District[i][j] == 'c' and meet == 1:
            District[i][j] = 0
            meet = 1
            move = 1
        elif District[i][j] == '.' and meet == 0:
            District[i][j] = -1
        elif District[i][j] == '.' and meet == 1:
            District[i][j] = move
            move += 1
for k in range(len(District)):
    print(*District[k])