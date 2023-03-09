SUM = []  # 숫자를 담을 리스트
for i in range(5):
    SUM.append(int(input()))
SUM.sort()
print(sum(SUM) // 5)  # 평균
print(SUM[len(SUM) // 2])  # 중앙값