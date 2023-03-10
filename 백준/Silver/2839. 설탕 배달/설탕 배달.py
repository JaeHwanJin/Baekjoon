N = int(input())
cnt = 0  # 3킬로그램 봉지에 담은 갯수
while N >= 0:
    if N % 5 == 0:  # 5로 나눠 떨어질때가 가장 작은수
        print(N // 5 + cnt)
        break
    N -= 3  # 5로 나눠떨어지지 않으면 3킬로그램 봉지에 담아야 하니 3을 빼준다.
    cnt += 1  # 3킬로그램 봉지에 담은 횟수
if N < 0:
    print(-1)