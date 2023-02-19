N = int(input())
arr = []
for i in range(N):
    num = int(input())
    arr.append(num)
arr = sorted(arr)

for j in arr:
    print(j)