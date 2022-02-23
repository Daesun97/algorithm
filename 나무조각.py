wood = list(map(int, input().split()))
target = [1, 2, 3, 4, 5]
while wood != target:
    for i in range(4):
        if wood[i] > wood[i+1]:
            wood[i],wood[i+1] = wood[i+1],wood[i]

    for j in range(5):
        print(wood[j],end=" ")
    print()