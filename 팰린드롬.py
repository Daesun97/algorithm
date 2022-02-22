T = int(input())

for i in range(T):
    k= int(input())
    word=[input() for j in range(k)]
# 단어조합하기
    new_word=[]
    for a in range(len(word)):
        for b in range(len(word)):
            if a!=b:
                n_word=word[a]+word[b]
                new_word.append(n_word)
# 조합된 단어에서 팔린드롬 찾기
    palin = []

    for c in range(len(new_word)):
        if new_word[c] == new_word[c][::-1]:
            pal=new_word[c]
            palin.append(pal)

#출력
    if len(palin)==0:
        print(0)
    else:
        print(palin[0])




