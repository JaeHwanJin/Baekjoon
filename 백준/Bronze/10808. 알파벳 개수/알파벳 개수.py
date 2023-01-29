inp = input()
word = 'abcdefghijklmnopqrstuvwxyz'
words = {}
result = ''
for i in word :
    words[i] = 0
for i in range(len(inp)) :
    if inp[i] in words :
        words[inp[i]] += 1
for i in words.values() :
    result += str(i) + ' '
print(result)