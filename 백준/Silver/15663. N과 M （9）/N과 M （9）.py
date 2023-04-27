N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
lst = []
visited = [0] * N

def back():
    if len(lst) == M:
        print(*lst)
        return
    exp_num = 0
    for i in range(N):
        if visited[i] == 0 and nums[i] != exp_num:
            visited[i] = 1
            exp_num = nums[i]
            lst.append(nums[i])
            back()
            lst.pop()
            visited[i] = 0

back()