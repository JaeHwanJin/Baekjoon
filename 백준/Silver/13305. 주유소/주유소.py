N = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))
price.pop()
cnt = 0
for i in range(len(price)):
    if price[i] != min(price):
        cnt += price[i] * length[i]
    else:
        cnt += price[i] * sum(length[i:])
        break
print(cnt)
