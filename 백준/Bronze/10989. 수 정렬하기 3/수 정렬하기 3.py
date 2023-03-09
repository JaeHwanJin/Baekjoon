import sys

num = [0] * 100001  # 10,000보다 작거나 같은 자연수리스트를 만들어준다.

for i in range(int(sys.stdin.readline())):
    num[int(sys.stdin.readline())] += 1  # 입력값의 인덱스에 1씩 추가 해준다.

for j in range(10001):
    if num[j] != 0:  # 해당 인덱스의 값이 0 이 아니라면 해당 인덱스를 인덱스의 값만큼 출력해준다.
        for k in range(num[j]):
            print(j)