from collections import deque
n=int(input())
ballon= deque(enumerate(map(int,input().split())))
ans=[]
for i in range(n):
    print(ballon[0][0]+1)
    jump=ballon.popleft()[1]
    if jump>0:
        ballon.rotate(-(jump-1))
    else:
        ballon.rotate(-jump)
