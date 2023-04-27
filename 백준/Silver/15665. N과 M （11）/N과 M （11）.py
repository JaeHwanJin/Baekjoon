N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums = list(set(nums))
nums.sort()

lst = []
visited = [0] * N

def back():
    if len(lst) == M:
        print(*lst)
        return
    for i in range(len(nums)):
        lst.append(nums[i])
        back()
        lst.pop()
back()
