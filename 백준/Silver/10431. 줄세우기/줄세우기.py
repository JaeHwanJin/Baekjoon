P = int(input())
student = [0] * 20
for p in range(P):
    T = list(map(int, input().split()))
    TC = T.pop(0)
    cnt = 0 # 뒤로 물러난 걸음 수
    for i in range(len(T)):
        for j in range(i+1, len(T)):
            if T[i] > T[j]:
                T[i], T[j] = T[j], T[i]
                cnt += 1
    print(TC, cnt)