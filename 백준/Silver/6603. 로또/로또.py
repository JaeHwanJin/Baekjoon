def lotto(start):
    if len(result) == 6:
        print(*result)
        return
    for i in range(start, len(nums)):
        if nums[i] not in result:
            result.append(nums[i])
            lotto(i+1)
            result.pop()

while True:
    nums = list(map(int, input().split()))
    result = []
    if nums[0] != 0:
        N = nums.pop(0)
        lotto(0)
        print()
    else:
        break