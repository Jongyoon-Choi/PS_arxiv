n=int(input())
for _ in range(n):
    tree=input()
    max=0
    stack=[]
    for t in tree:
        if t==']':
            if len(stack)>max:
                max=len(stack)
            stack.pop()
        else:
           stack.append(t)
    print(2**max)