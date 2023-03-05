day, ran = map(int, input().split())  # 날짜와 범위
tem = list(map(int, input().split()))  # 온도
SUM = sum(tem[:ran])  # 첫 번째 범위의 온도 합
MAX = SUM
for i in range(ran, day):
    # 다음 온도 합은 직전 온도합 + 다음 범위 첫번째 값 + 직전 온도 합 연속된 날짜 첫번째 값
    SUM = SUM + tem[i] - tem[i - ran]
    if MAX < SUM:
        MAX = SUM
print(MAX)