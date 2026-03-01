n=int(input())
stack=[]
next=1
res=[]
for i in range(n):
    m=int(input())
    while not stack or stack[-1]<m:
        stack.append(next)
        next+=1
        res.append('+')
    if stack[-1]==m:
        stack.pop()
        res.append('-')
    else:
        res=['NO']
        break
for char in res:
    print(char)