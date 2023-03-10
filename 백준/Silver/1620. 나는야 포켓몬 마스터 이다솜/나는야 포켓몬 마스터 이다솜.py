import sys

N, M = map(int, sys.stdin.readline().split())
poket = dict()

for i in range(1, N + 1):
    inp = sys.stdin.readline().strip()
    poket[str(i)] = inp
    poket[inp] = i

for j in range(M):
    ques = sys.stdin.readline().strip()
    if ques in poket.keys():
        print(poket[ques])