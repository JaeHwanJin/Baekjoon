M = int(input())
N = int(input())
prime_number = []
for i in range(M, N + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:  # 약수 구하기  
            cnt += 1
    if cnt == 2:  # 약수가 2개뿐이면 소수
        prime_number.append(i)

if len(prime_number) > 0:
    print(sum(prime_number))
    print(min(prime_number))
else:
    print(-1)