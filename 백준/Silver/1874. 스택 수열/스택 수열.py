N = int(input())

num, result = [], []
cnt = 0

for i in range(N):
    n = int(input())

    while cnt < n:
        cnt += 1
        num.append(cnt)
        result.append('+')

    if num[-1] == n:
        num.pop()
        result.append('-')

if len(num) == 0:
    for l in result:
        print(l)
else:
    print('NO')