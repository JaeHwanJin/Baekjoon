def solution(n):
    answer = (str(bin(n)))[2:]
    result = 0
    while True:
        n += 1
        result = (str(bin(n)))[2:]
        if answer.count("1") == result.count("1"):
            break
    return n