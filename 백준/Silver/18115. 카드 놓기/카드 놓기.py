import sys
from collections import deque

n=int(sys.stdin.readline())
act=sys.stdin.readline().split()
res=deque()
for i in range(1,n+1):
    cmd=act.pop()
    if cmd=='1':
        res.appendleft(i)
    elif cmd=='2':
        res.insert(1,i)
    else:
        res.append(i)
print(' '.join(map(str,res)))