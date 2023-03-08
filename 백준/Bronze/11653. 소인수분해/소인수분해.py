N = int(input())
result = []
cnt = 2 # 약수를 구하기 위한 값
while N != 1:
    if N % cnt == 0:    # 나눠서  나머지가 0이면 약수
        result.append(cnt)
        N = N // cnt
    else:   # 나머지가 0이 아니면 cnt+1해서 약수확인
        cnt += 1

for i in result:
    print(i)