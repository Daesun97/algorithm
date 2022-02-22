P = input()
P_reverse = ""
P_lis = []

for i in P:
    P_lis.append(i)

P_lis.reverse()

for i in P_lis:
    P_reverse +=i
if P==P_reverse:
    print(1)
else:
    print(0)
