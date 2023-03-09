N, K = map(int, input().split())
score = list(map(int, input().split()))
score.sort()    # 점수 순으로 정렬
print(score[-K])    # K번의 점수가 커트라인