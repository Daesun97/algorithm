players= input().split()
foul= {}

for player in players:
    if player not in foul:
        foul[player] = 1
    else:
        foul[player]+= 1

for key in foul.keys():
    if foul[key]== min(foul.values()):
        print(key)

print(min(foul.values()))
