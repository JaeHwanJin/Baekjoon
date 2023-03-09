import sys

result = []
for i in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    result.append([x, y])  # x와 y 좌표를 하나의 리스트에 담아 result리스트에 추가
result.sort()  # 오름정렬
for i in range(len(result)):
    print(*result[i])  # []빼고 리스트 안의 값만 출력