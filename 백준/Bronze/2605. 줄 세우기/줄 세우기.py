# 첫째 줄에는 학생의 수가 주어지고
N = int(input())
# 둘째 줄에는 줄을 선 차례대로 학생들이 뽑은 번호가 주어진다.
line_num = list(map(int, input().split()))
student = [] # 학생 수만큼 번호부여 list
result = [] # 급식 순서를 담을 list
for i in range(1, N+1):
    student.append(i)   # 번호 부여
    result.append(0)    # 학생 수 만큼 list크기 늘리기
for j in range(len(line_num)):
    result.insert(line_num[j], student[j])  # 뽑은 번호가 자신의 순서이고 기존에 사람이 있다면 그 사람 뒤로
print(*result[N-1::-1])