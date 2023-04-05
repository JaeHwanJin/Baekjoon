from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    STR = input().strip()
    P = int(input())
    q = deque(input().strip()[1:-1].split(','))
    e = 0  # error 발생횟수
    cnt = 0 # R 횟수

    if P == 0 :
        q = deque()

    for i in STR:
        if i == 'R':
            cnt += 1
        else:
            if len(q) == 0:
                print('error')
                break
            else:
                if cnt % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
            # if cnt % 2 == 0:
            #     cnt = 0
            #     try:
            #         q.popleft()
            #     except:
            #         e = 1
            # else:
            #     cnt = 0
            #     try:
            #         q.reverse()
            #         q.popleft()
            #     except:
            #         e = 1
    else:
        if cnt % 2 == 0:
            print('[' + ','.join(q) + ']')
        else :
            q.reverse()
            print('[' + ','.join(q) + ']')