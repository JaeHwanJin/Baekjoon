import sys
x = list(map(int, sys.stdin.readline().split()))
print((pow(x[0], 2)+pow(x[1], 2)+pow(x[2], 2)+pow(x[3], 2)+pow(x[4], 2))%10)