N, K = map(int, input().split())
coin = []

for i in range(N):
    coin.append(int(input()))
coin.sort(reverse=True)
cnt = 0
for j in range(N):
    if K >= coin[j]:
        cnt += K // coin[j]
        K = K % coin[j]
print(cnt)