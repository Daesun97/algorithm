score=[]
for i in range(5):
    score.append(list(map(int,input().split())))

    #score.append(list(map(int,input().split())))

winer_sc=0
winer_idx=0
for i in range(5):
    if winer_sc < sum(score[i]):
        winer_sc=sum(score[i])
        winer_idx =1+i

print(f"{winer_idx} {winer_sc}")
