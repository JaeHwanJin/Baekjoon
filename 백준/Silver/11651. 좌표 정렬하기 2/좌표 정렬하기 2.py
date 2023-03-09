import sys

result = []
for n in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    result.append([y, x])

result.sort()

for i, j in result:
    print(j, i)