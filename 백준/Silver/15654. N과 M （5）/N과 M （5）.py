N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []
def back():
    if len(result) == M:
        print(*result)
        return
    for i in nums:
        if i not in result:
            result.append(i)
            back()
            result.pop()
back()