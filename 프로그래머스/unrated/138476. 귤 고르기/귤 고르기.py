from collections import Counter

def solution(num, arr):
    answer = Counter(arr)
    answer = sorted(list(answer.values()), reverse=True)
    cnt = 0
    for i in answer:
        print(i)
        num -= i
        cnt += 1
        if num <= 0 :
            break
    return cnt 