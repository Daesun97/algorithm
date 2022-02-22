c = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
w = input()
for i in c:
    w=w.replace(i,"2")
print(len(w))