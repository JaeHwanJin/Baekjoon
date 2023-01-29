while True :
    cnt = 0
    inp = input()
    if inp == '#' :
        break
    else :
        for i in inp :
            if i in 'aeiouAEIOU' :
                cnt += 1
            else :
                continue
    print(cnt)