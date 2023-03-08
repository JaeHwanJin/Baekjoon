N, K = map(int, input().split())

result = []
for i in range(1, N + 1):
    if N % i == 0:  # 나눴을때 몫이 0 이면 약수
        result.append(i)
if len(result) >= K:  # index 에러를 방지하기 위해
    print(result[K - 1])
else:  # K번째 약수가 존재하지 않을경우 0출력
    print(0)