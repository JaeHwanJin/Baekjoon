N = int(input())
arr = []

for i in range(N):
    num = int(input())
    arr.append(num)
for k in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
for l in arr:
    print(l)
