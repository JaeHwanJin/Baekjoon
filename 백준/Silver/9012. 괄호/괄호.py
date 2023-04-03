for tc in range(int(input())):
    str = input()
    stack = []
    for i in str:
        if i == '(':
            stack.append(i)
        else:
            try:
                stack.pop()
            except:
                print('NO')
                break
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')