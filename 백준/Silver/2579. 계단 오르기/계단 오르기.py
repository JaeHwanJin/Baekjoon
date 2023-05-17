import sys
input = sys.stdin.readline

n=int(input()) # 계단 개수
score=[int(input()) for _ in range(n)] # 계단 리스트
dp=[0]*(n) # dp 리스트
if len(score)<=2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(score))
else: # 계단이 3개 이상일 때
    dp[0]=score[0] # 첫째 계단 수동 계산
    dp[1]=score[0]+score[1] # 둘째 계단까지 수동 계산
    for i in range(2,n): # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
        dp[i]=max(dp[i-3]+score[i-1]+score[i], dp[i-2]+score[i])
    print(dp[-1])