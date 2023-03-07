N, M = map(int, input().split())
num = []
for i in range(0, N + 1):  # list의 index는 0부터 시작하기때문에
    num.append(i)
for j in range(M):
    st, end, mid = map(int, input().split())
    cnt = 0
    for k in range(mid, end + 1):  # mid부터 end index의 값 찾아서 위치 변경
        NUM = num[k]
        del num[k]
        num.insert(st + cnt, NUM)
        cnt += 1
print(*num[1:])