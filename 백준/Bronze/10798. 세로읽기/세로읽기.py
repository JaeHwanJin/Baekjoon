STR = [list(map(str, input())) for _ in range(5)]
for j in range(15):
    for i in range(5):
        if j < len(STR[i]): # j보다 작으면 index오류 발생하기 때문에
            print(STR[i][j], end='')