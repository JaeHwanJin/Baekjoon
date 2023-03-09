import sys

num = []
for inp in range(int(sys.stdin.readline().strip())):
    num.append(int(sys.stdin.readline().strip()))  # 입력 값 리스트에 추가

num.sort()  # 리스트 오름차순 정렬

print(round(sum(num) / len(num)))  # 산술평균
print(num[len(num) // 2])  # 중앙값

mode = dict()
for i in num:
    if i in mode:
        mode[i] += 1
    else:
        mode[i] = 1
MAX = max(mode.values())  # 최빈값
MAX_dic = []  # 최빈값을 저장 할 list

for j in mode:
    if MAX == mode[j]:
        MAX_dic.append(j)

if len(MAX_dic) > 1:  # 최빈값이 여러개라면    
    print(MAX_dic[1])  # 두번째로 작은 값
else:
    print(MAX_dic[0])   # 최빈값

print(max(num) - min(num))  # 범위 : 최댓값과 최솟값의 차이