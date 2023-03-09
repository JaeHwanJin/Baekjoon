N = int(input())
X = list(map(int, input().split()))
newX = list(sorted(set(X)))  # 좌표마다 순서를 부여하기 위해 중복을 제거하고 정렬해준다.
ind = dict()  # 좌표와 숫자 조합의 딕셔너리

for i in range(len(newX)):  # 각 좌표에 순서를 부여
    ind[newX[i]] = i

for j in range(len(X)): # 해당 좌표가 있을 경우 해당 좌표의 순서를 출력
    if X[j] in ind.keys():
        print(ind[X[j]], end=" ")