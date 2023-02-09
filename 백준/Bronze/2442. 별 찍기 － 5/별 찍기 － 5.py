num = int(input())

star = '*'
for i in range(1, num + 1):
    print((' ' * (num - i)) + (star * (2 * i - 1)))