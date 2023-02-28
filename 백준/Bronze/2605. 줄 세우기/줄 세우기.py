# 첫째 줄에는 학생의 수가 주어지고
N = int(input())
# 둘째 줄에는 줄을 선 차례대로 학생들이 뽑은 번호가 주어진다.
line_num = list(map(int, input().split()))
student = []
result = []
for i in range(1, N+1):
    student.append(i)
    result.append(0)
for j in range(len(line_num)):
    result.insert(line_num[j], student[j])
print(*result[N-1::-1])