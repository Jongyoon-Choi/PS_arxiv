n=int(input())
line=list(map(lambda x: {'W':-1, 'M':1}[x],input()))
gap=0
count=0
while line:
    if gap==0:
        gap+=line.pop(0)
    elif gap>0:
        if -1 in line[:2]:
            line.remove(-1)
            gap-=1
        else:
            gap+=line.pop(0)
    else:
        if 1 in line[:2]:
            line.remove(1)
            gap+=1
        else:
            gap+=line.pop(0)
    if abs(gap)>n:
        break
    count+=1
print(count)