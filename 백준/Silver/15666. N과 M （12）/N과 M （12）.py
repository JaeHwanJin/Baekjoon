N, M = map(int, input().split())
nums = list(set(list(map(int, input().split()))))
nums.sort()
lst = []


def back(start):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(start, len(nums)):
        lst.append(nums[i])
        back(i)
        lst.pop()


back(0)