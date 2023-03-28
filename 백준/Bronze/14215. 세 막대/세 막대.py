a, b, c = map(int, input().split())
arr = [a, b, c]
arr.sort()
if arr[0] + arr[1] > arr[2]:
    print(arr[0] + arr[1] + arr[2])
else:
    print((arr[0] + arr[1]) * 2 - 1)