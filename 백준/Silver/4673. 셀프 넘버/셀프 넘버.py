def d(n):
    n = str(n)
    x = []
    y = 0
    for i in range(len(n)):
        x.append(int(n[i]))
        y += x[i]
    n = int(n)
    return n + y

is_not_selfnumber = set()

for i in range(1, 10001):
    is_not_selfnumber.add(d(i))

for j in range(1, 10001):
    if j not in is_not_selfnumber:
        print(j)