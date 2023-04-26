N, S = map(int, input().split())
result = list(map(int, input().split()))
lst = []
cnt = 0


def back(start):
    global cnt
    # print(lst)
    if sum(lst) == S and len(lst) > 0:
        cnt += 1
    for i in range(start, len(result)):
        lst.append(result[i])
        back(i + 1)
        lst.pop()

back(0)
print(cnt)