lis1=input()
num_lis1=[list(map(int,input().split())) for i in range(2)]
lis2=input()
num_lis2=[list(map(int,input().split())) for i in range(2)]

for i in range(2):
    print([num_lis1[i][j]*num_lis2[i][j] for j in range(4)])
#print([num_lis1[i][j]*num_lis2[i][j] for i in range(2) for j in range(4)])


