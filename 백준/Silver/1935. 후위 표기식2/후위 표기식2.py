N=int(input())
expression=list(input())
value=[]
res=[]
for _ in range(N):
    value.append(int(input()))
for char in expression:
    if char>='A' and char<='Z':
        res.append(value[ord(char)-ord('A')])
    elif char=='+':
        res.append(res.pop(-2)+res.pop())
    elif char=='-':
        res.append(res.pop(-2)-res.pop())
    elif char=='*':
        res.append(res.pop(-2)*res.pop())
    else:#/
        res.append(res.pop(-2)/res.pop())
print('{:.2f}'.format(res.pop()))