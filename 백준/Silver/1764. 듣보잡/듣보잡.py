import sys
N, M = map(int, sys.stdin.readline().split())
dj = set()
bj = set()

for i in range(N):
    dj.add(sys.stdin.readline().rstrip())
for j in range(M):
    bj.add(sys.stdin.readline().rstrip())

result = sorted(dj & bj)
print(len(result))
for k in result:
    print(k)