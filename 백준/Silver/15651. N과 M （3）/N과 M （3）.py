N, M = map(int, input().split())
result = []


def back():
    if len(result) == M :
        print(*result)
        return
    for i in range(1, N + 1):
        # if i not in result:
        result.append(i)
        back()
        result.pop()
back()