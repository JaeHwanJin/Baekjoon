num = int(input())
nums = map(int, input().split())
cnt = 0
for i in nums :
    if num == i :
        cnt += 1
print(cnt)