L = int(input())  # 롤케이크의 길이
N = int(input())  # 방청객의 수
cake = [0] * (L+1)  # 1미터 단위로 잘라진 롤케이크
num = 1  # 첫번재 방청객번호
real = []   # 실제로 방청객이 받은 케이크 수 리스트
MAX = [] # 가장 많은 조각을 받을 것으로 기대하고 있던 방청객의 케이크 수 리스트
for n in range(N):
    cnt = 0
    st, end = map(int, input().split()) # 방청객이 원하는 케이크 범위
    MAX.append(end - st)    # 가장 많은 조각을 받을 것으로 기대하고 있던 방청객의 케이크 수
    for i in range(st, end + 1):
        if cake[i] == 0:    # 번호가 매겨져 있지 않은곳에 체크
            cake[i] = num   # 방청객 번호
            cnt += 1    # 해당 방청객이 실제로 가져갈 수 있는 케이크 수
    num += 1    # 방청객 번호 1씩 증가
    real.append(cnt)

print(MAX.index(max(MAX)) + 1)
print(real.index(max(real)) + 1)