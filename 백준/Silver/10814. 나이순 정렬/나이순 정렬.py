import sys

N = int(input())
result = []
for i in range(N):
    age, name = sys.stdin.readline().strip().split()
    result.append([int(age), name])

result = sorted(result, key=lambda x: x[0])

for j in result:
    print(*j)