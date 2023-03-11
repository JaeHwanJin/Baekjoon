import sys
S = sys.stdin.readline().rstrip()

result = set()
for i in range(len(S)):
    for j in range(i, len(S)):  # i부터 시작하지 않으면 빈값 존재
        result.add(S[i:j+1])

print(len(result))