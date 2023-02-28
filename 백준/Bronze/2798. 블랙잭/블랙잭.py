N, M = map(int, input().split())
card = list(map(int, input().split()))
SUM = 300001
result = 0
for i in card:
    for j in card:
        for k in card:
            if k != i != j != k and i + j + k <= M:
                SUM = i + j + k
                if result <= SUM:
                    result = SUM
print(result)