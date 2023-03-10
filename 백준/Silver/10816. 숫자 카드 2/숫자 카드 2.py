import sys
from collections import Counter
N = int(sys.stdin.readline())  # 상근이가 가지고 있는 카드
Nnum = map(str, sys.stdin.readline().split())

M = int(sys.stdin.readline())  # 가지고 있는지 확인 할 카드
Mnum = map(str, sys.stdin.readline().split())

result = Counter(Nnum)

for i in Mnum:
    if i in result:
        print(result[i], end=' ')
    else:
        print(0, end=' ')