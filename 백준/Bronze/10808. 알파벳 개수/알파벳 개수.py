cnt = [0] *26
inp = input()
for i in inp :
    cnt[ord(i)-97] += 1
for i in cnt :
    print(i, end=' ')