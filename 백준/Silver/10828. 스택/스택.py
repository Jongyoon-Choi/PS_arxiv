import sys
n=int(sys.stdin.readline())
stack=[]
for i in range(n):
    ipt=sys.stdin.readline().split()
    if ipt[0]=='push':
        stack.append(int(ipt[1]))
    elif ipt[0]=='size':
        print(len(stack))
    elif ipt[0]=='empty':
        print(int(len(stack)==0))
    elif not stack:
        print(-1)
    elif ipt[0]=='pop':
        print(stack.pop())
    elif ipt[0]=='top':
        print(stack[-1])