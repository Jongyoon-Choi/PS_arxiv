import sys
n=int(sys.stdin.readline())
lst=[]
for i in range(n):
    ipt=sys.stdin.readline().split()
    if ipt[0]=='push':
        lst.append(int(ipt[1]))
    elif ipt[0]=='size':
        print(len(lst))
    elif ipt[0]=='empty':
        print(int(len(lst)==0))
    elif not lst:
        print(-1)
    elif ipt[0]=='front':
        print(lst[0])
    elif ipt[0]=='back':
        print(lst[-1])
    else:#pop
        print(lst.pop(0))