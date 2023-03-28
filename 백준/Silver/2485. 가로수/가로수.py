import sys
import math

N = int(input())
arr = [int(input()) for i in range(N)] # 심겨져있는 가로수
arr2 = [] # 심겨져있는 가로수들의 거리

for i in range(1,len(arr)):
    arr2.append(arr[i] - arr[i-1])

d = math.gcd(*arr2) # 심겨져 있는 가로수들의 거리의 최대공약수
cnt = 0

for j in arr2:
    cnt += (j // d) -1
print(cnt)