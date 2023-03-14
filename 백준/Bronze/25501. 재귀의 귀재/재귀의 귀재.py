def recursion(s, st, end):
    global cnt  # 호출 회수 cnt를 사용하기 위한 global cnt 
    cnt += 1    # recursion 함수 호출시마다 cnt 1씩 증가
    if st >= end:
        return 1
    elif s[st] != s[end]:
        return 0
    else:
        return recursion(s, st + 1, end - 1)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)


for i in range(int(input())):
    cnt = 0 # 호출 회수
    print(isPalindrome(input()), cnt)