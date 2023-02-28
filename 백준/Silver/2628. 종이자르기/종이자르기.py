row, col = map(int, input().split())
l = [0]
h = [0]
n = int(input())
for tc in range(n):
    a, b = map(int, input().split())
    if a == 0:
        h.append(b)
    else:
        l.append(b)
l.append(row)
h.append(col)
l.sort()
h.sort()
# print(l)
# print(h)
L = 0
H = 0
for i in range(0, len(l) - 1):
    a = l[i+1] - l[i]
    if L < a:
        L = a
        # print('l', L)
for j in range(0, len(h) - 1):
    b = h[j + 1] - h[j]
    if H < b:
        H = b
        # print('h', H)
print(L * H)