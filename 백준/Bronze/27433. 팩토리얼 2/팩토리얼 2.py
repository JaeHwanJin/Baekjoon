def fibonacci(N):
    if N <= 1:
        return 1
    return N * fibonacci(N - 1)


print(fibonacci(int(input())))