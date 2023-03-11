import sys

A, B = map(int, sys.stdin.readline().split())
Anum = set(map(int, sys.stdin.readline().split()))
Bnum = set(map(int, sys.stdin.readline().split()))
print(len(Anum - Bnum) + len(Bnum - Anum))