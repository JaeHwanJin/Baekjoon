import sys

N, M = map(int, sys.stdin.readline().split())

Nstr = set()  # 집합 S
for i in range(N):
    Nstr.add(sys.stdin.readline().rstrip())

Mstr = dict()  # 검사 해야 하는 문자 집합
for j in range(M):
    x = sys.stdin.readline().rstrip()
    if x in Mstr:
        Mstr[x] += 1
    else:
        Mstr[x] = 1

SUM = 0

for i in Nstr:
    if i in Mstr.keys():
        SUM += Mstr[i]
print(SUM)