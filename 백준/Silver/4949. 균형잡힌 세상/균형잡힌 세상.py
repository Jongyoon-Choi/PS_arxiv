while True:
    ipt=list(input())
    if ipt[0]=='.':
        break
    filtered_ipt=[char for char in ipt if char in '()[]']
    stack=[]
    for i in filtered_ipt:
        if i=='(' or i=='[':
            stack.append(i)
        elif not stack:
            stack.append('no')
            break
        elif i==')' and stack[-1]=='(':
            stack.pop()
        elif i==']' and stack[-1]=='[':
            stack.pop()
        else:
            stack.append('no')
            break
    if not stack:
        print('yes')
    else:
        print('no')