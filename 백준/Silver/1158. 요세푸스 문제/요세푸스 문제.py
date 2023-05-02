from collections import deque

N, K = map(int, input().split())

# 1부터 N까지의 숫자를 큐에 넣음
q = deque(range(1, N+1))

# 요세푸스 순열을 담을 리스트 초기화
josephus = []

# 큐에 원소가 남아있는 동안 반복
while len(q) > 1:
    # K-1번째까지의 원소를 맨 뒤로 보냄
    for _ in range(K-1):
        q.append(q.popleft())
    # K번째 원소를 제거하고 요세푸스 순열에 추가함
    josephus.append(q.popleft())

# 마지막으로 남은 하나의 원소를 요세푸스 순열에 추가함
josephus.append(q[0])

# 요세푸스 순열을 출력
print('<' + ', '.join(map(str, josephus)) + '>')