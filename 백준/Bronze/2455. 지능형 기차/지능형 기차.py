IN = 0
MAX = 0
for i in range(4):
    x, y = map(int, input().split())
    IN -= x
    IN += y
    if IN > MAX:
        MAX = IN
print(MAX)