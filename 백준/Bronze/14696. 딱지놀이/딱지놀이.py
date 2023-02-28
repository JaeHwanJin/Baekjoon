N = int(input())
for tc in range(N):
    A = list(map(int, input().split()))[1::]  # 0번째는 카드의 개수라 제외
    B = list(map(int, input().split()))[1::]  # 0번째는 카드의 개수라 제외
    for i in range(4, 0, -1):
        if A.count(i) > B.count(i):  # 4 3 2 1 순으로 많은 카드를 가지고 있으면 승리
            print('A')
            break
        elif A.count(i) < B.count(i):
            print('B')
            break
        elif i == 1:  # 모두 비교했는데 값이 같다면 무승부
            print('D')
            break