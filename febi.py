a = []
for i in range(4):
    b = []
    for j in range(4):
        if i == j:
            b.append(1)
        elif j > i:
            b.append(1)
        else:
            b.append(0)
    a.append(b)
for i in range(len(a)):
    print("|",end="")
    for j in range(len(a[0])):
        print("%4d"%(a[i][j]),end="")
    print("%4s"%"|")