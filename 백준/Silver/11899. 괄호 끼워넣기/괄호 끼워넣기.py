expr=list(input())
stack=[]
for char in expr:
    if char==')' and stack and stack[-1]=='(':
        stack.pop()
    else:
        stack.append(char)
print(len(stack))