N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
lst = []


def back(start):
    if len(lst) == M:
        print(*lst)
    for i in range(start, len(nums)):
        if nums[i] not in lst:
            lst.append(nums[i])
            back(i + 1)
            lst.pop()

back(0)