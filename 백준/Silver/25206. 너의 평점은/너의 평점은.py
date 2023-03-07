avg = 0
SUM = 0
# 등급 별 과목평점
GRADE = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F' : 0.0}
for tc in range(20):
    name, score, grade = input().split()
    if grade != 'P':
        avg += (float(score) * GRADE[grade])  # (학점 * 과목평점)
        SUM += float(score)  # 학점의 총합
result = avg / SUM
print(result)