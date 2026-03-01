n=list()
for i in range(9):
    n.append(int(input()))
tf=False
for j in range(8):
    for k in range(j+1,9):
        if sum(n)-n[j]-n[k]==100:
            n.remove(n[k])
            n.remove(n[j])
            tf=True
            break
    if tf:
        break
n.sort()
for i in range(7):
    print(n[i])