square = int(input())
cnt = 0
for i in range(1, square + 1):   # 만들 수 있는 직사각형의 갯수는 각 수의 약수의 개수
    for j in range(i, square + 1):
        if i * j <= square:
            cnt += 1
print(cnt)