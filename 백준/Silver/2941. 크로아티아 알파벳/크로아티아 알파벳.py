cword = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for i in range(len(cword)):
    if cword[i] in word:    # 크로아티아 알파벳에 해당하는 문자열은 하나의 문자로 카운트 해줘야 하기 때문에
        word = word.replace(cword[i], '/')

print(len(word))
