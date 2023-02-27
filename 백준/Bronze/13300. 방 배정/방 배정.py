N, K = map(int, input().split())
M, W = [0] * 7, [0] * 7
cnt = 0
for tc in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        W[Y] += 1
    else:
        M[Y] += 1
for i in range(len(M)):
    if M[i] != 0:
        if M[i] % 2 == 0:
            cnt += M[i] // 2
        else:
            cnt += M[i] // 2 + 1
for i in range(len(W)):
    if W[i] != 0:
        if W[i] % 2 == 0:
            cnt += W[i] // 2
        else:
            cnt += W[i] // 2 + 1
print(cnt)