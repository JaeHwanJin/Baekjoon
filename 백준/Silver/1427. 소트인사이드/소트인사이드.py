import sys

N = list(map(int, sys.stdin.readline().strip()))

N.sort(reverse=True)
for i in N:
    print(i, end='')