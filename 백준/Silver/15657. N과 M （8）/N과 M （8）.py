N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
lst = []


def back(start):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(start, N):
        lst.append(nums[i])
        back(i)
        lst.pop()

back(0)