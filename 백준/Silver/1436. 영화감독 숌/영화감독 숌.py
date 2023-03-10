N = int(input())
cnt = 0
n = 666
while True:
    if '666' in str(n):
        cnt += 1
    if cnt == N:
        print(n)
        break
    n += 1