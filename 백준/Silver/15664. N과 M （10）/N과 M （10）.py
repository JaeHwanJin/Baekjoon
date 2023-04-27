def back(start):
    if len(lst) == M:
        print(*lst)
        return
    exp_num = 0
    for i in range(start, N):
        if visited[i] == 0 and exp_num != nums[i]:
            lst.append(nums[i])
            visited[i] = 1

            exp_num = nums[i]

            back(i+1)

            lst.pop()
            visited[i] = 0

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

lst = []
visited = [0] * N

back(0)