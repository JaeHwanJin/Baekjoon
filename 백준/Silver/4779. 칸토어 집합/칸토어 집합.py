def kan(n):
    N = 3 ** (n - 1)
    if n == 0:
        return '-'
    return kan(n - 1) + (' ' * N) + kan(n - 1)


while True:
    try:
        print(kan(int(input())))
    except:
        break