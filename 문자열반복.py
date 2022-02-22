r = int(input())

for i in range(r):
    R,S=input().split()
    text=""
    
    for i in S:
        text += int(R)*i
    print(text)

    
