n=int(input())
for i in range(n):
    count=0
    stack=list(input())
    while stack:
        if stack.pop()==')':
            count+=1
        else:
            count-=1
        if count < 0:
            break
    if count==0:
        print('YES')
    else:
        print('NO')