N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
lst = []
def back():
    if len(lst) == M:
        print(*lst)
        return
    for i in nums:
        lst.append(i)
        back()
        lst.pop()
        
back()