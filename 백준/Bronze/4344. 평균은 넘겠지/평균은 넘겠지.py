import sys

x = int(sys.stdin.readline())

for i in range(x):
    y = list(map(int, sys.stdin.readline().split()))
    z = sum(y[1:])/y[0]
    count = 0
    for i in y[1:]:
        if i > z:
            count += 1
    result = (count/len(y[1:]))*100
    print('{0:0.3f}%'.format(result))