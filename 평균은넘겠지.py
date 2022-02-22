C = int(input())
results = []
for i in range(C):
    C_average = list(map(int, input().split()))
    C_average_num = C_average[0]
    scores = C_average[1:]
    score_mean = sum(scores)/C_average_num

    gosu = 0

    for score in scores:
        if score > score_mean:
            gosu +=1
    
    results.append(round((gosu/C_average_num)*100,3))

for result in results:
    print("{:.3}%".format(result))



