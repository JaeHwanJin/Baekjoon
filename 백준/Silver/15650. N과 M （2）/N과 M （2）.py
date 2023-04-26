N, M = map(int, input().split())
result = []
visited = []


def back(start):
    if len(result) == M :
        visited
        print(*result)
        return
    for i in range(start, N + 1):
        if i not in result:
            result.append(i)
            back(i+1)
            result.pop()
back(1)