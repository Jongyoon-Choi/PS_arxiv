s=input()+' '
res=''
stack=[]
fixed=False
for char in s:
    if fixed:
        res+=char
    else:
        stack.append(char)
    if char=='<':
        stack.pop()
        fixed=True
        for _ in range(len(stack)):
            res+=stack.pop()
        res+=char
    elif char=='>':
        fixed=False
    elif not fixed and char==' ':
        stack.pop()
        for _ in range(len(stack)):
            res+=stack.pop()
        res+=char
print(res[:-1])