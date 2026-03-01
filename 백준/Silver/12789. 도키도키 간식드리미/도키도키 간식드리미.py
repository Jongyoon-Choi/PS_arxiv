N=int(input())
line=list(map(int, input().split()))
next=1
stack=[]
while next<=N:
    if stack and stack[-1]==next:
        stack.pop()
        next+=1
    elif line and line[0]>next:
        stack.append(line.pop(0))
    elif line and line[0]==next:
        line.pop(0)
        next+=1
    else:
        break
print('Nice'if next>N else 'Sad')