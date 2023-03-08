N = int(input())
num = list(map(int, input().split()))
result = 0
for i in range(len(num)):
    cnt = 0
    for j in range(1, num[i] + 1):
        if num[i] % j == 0:  # 약수 구하기
            cnt += 1
    if cnt == 2:  # 약수가 2개뿐이라면 자신과 1만 약수인것이니 소수 이다.
        result += 1
print(result)