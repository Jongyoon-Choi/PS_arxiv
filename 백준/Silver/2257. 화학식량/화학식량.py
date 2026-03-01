cmd=list(input())
res=[]
for c in cmd:
    if c=='H':
        res.append(1)
    elif c=='C':
        res.append(12)
    elif c=='O':
        res.append(16)
    elif c=='(':
        res.append(c)
    elif c==')':
        if res[-1]=='(':
            res.pop()
        else:
            while res[-2]!='(':
                res.append(res.pop()+res.pop())
            res.pop(-2)
    else:#2~9
        res[-1]*=int(c)
print(sum(res))