expr=list(input())
res=[]
for char in expr:
    if char.isdigit():
        res.append(int(char))
    elif char=='+':
        res.append(res.pop(-2)+res.pop())
    elif char=='-':
        res.append(res.pop(-2)-res.pop())
    elif char=='*':
        res.append(res.pop(-2)*res.pop())
    elif char=='/':
        res.append(res.pop(-2)/res.pop())
print(int(res.pop()))