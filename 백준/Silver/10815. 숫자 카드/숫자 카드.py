import sys
input = sys.stdin.readline

N = int(input())
Nnum = set(map(int, input().split()))  # 상근이가 가지고 있는 카드

M = int(input())
Mnum = list(map(int, input().split()))  # 확인 할 카드

# result = dict()  # 가지고 있는지 아닌지 1과 0으로 구분하기 위한 딕셔너리

for i in Mnum:
    if i in Nnum:  # 가지고 있으면 1
        print(1,end=' ')
    else:  # 가지고 있지 않으면 0
        print(0,end=' ')