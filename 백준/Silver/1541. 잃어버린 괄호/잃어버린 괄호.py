arr = input().split('-')

SUM = 0

for i in arr[0].split('+'):
    SUM += int(i)

for i in range(1, len(arr)):
    for j in arr[i].split('+'):
        SUM -= int(j)

print(SUM)