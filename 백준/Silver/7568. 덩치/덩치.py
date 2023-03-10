import sys

N = int(input())
man = []  # [몸무게, 키]를 담을 리스트
for inp in range(N):
    man.append(list(map(int, sys.stdin.readline().split())))

result = []  # 등수를 담을 리스트
for i in range(len(man)):
    cnt = 1 # 1등부터 시작
    for j in range(len(man)):
        if man[i][0] < man[j][0] and man[i][1] < man[j][1]:
            cnt += 1
    result.append(cnt)

print(*result)