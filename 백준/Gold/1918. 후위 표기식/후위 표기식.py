expression=list(input())
stack=[]
res=''
for char in expression:
    if char>='A' and char<='Z':
        res+=char
    elif char == '(':
        stack.append(char)
    elif char == ')':
        while stack[-1]!='(':
            res+=stack.pop()
        stack.pop()
    elif char in '*/':
        if stack and stack[-1] in '*/':
            res+=stack.pop()
        stack.append(char)
    else:#+-
        while stack and stack[-1] in '+-*/':
            res+=stack.pop()
        stack.append(char)
while stack:
    res+=stack.pop()
print(res)