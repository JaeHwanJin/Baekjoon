N, M = map(int, input().split())
result = []


def back(start):
    if len(result) == M :
        print(*result)
        return
    for i in range(start, N + 1):
        # if i not in result:
        result.append(i)
        back(i)
        result.pop()
back(1)