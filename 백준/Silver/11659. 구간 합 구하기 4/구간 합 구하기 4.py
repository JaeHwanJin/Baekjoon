import sys
input = sys.stdin.readline
# 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다.
N, M = map(int, input().split())

# 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다.
arr = list(map(int, input().split()))
SUM = 0
SUM_arr = [0]
for k in arr:
    SUM += k
    SUM_arr.append(SUM)
    
# 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.
for _ in range(M):
    i, j = map(int, input().split())
    print(SUM_arr[j] - SUM_arr[i - 1])