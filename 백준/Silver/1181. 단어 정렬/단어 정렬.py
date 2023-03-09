import sys

N = int(input())
word = []
result = []

for i in range(N):
    word.append(sys.stdin.readline().strip())
word = list(set(word))

for j in range(len(word)):
    result.append([word[j], len(word[j])])

result = sorted(result, key=lambda x: [x[1], x[0]])
for x, y in result:
    print(x)