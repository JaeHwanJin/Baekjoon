word = input()
lword = len(word)

# 슬라이싱을 활용해 앞 뒤를 비교

if lword % 2 == 0 and word[:lword // 2] == word[lword:lword // 2 - 1:-1]:
    print(1)

elif lword % 2 != 0 and word[:lword // 2] == word[lword:lword // 2:-1]:
    print(1)
# 위 두가지를 제외한 경우는 모두 팰린드롬이 아니다.
else:
    print(0)