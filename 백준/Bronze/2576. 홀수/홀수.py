arr = []
SUM = 0
MIN = 10000
for tc in range(7):
    num = int(input())
    if num % 2 == 1:
        arr.append(num)
        if num < MIN:
            MIN = num
        SUM += num
    else:
        continue

if len(arr) == 0:
    print(-1)
else:
    print(SUM)
    print(MIN)