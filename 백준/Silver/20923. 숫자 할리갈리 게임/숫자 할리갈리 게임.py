from collections import deque
import sys

n, m=map(int, sys.stdin.readline().split())
start=[deque(), deque()]
temp=[deque(), deque()]
check=[0, 0]
for _ in  range(n):
    d, s = map(int, sys.stdin.readline().split())
    start[0].append(d)
    start[1].append(s)
t=0
for _ in range(m):
    check[t]=start[t].pop()
    temp[t].append(check[t])
    if not start[t]:
        break
    win=-1
    for i in [0,1]:
        if temp[i] and check[i]==5: # 둘중 하나가 5
            win=0
    if temp[0] and temp[1] and sum(check)==5: 
            win=1
    if win!=-1:
        start[win].extendleft(temp[1-win])
        start[win].extendleft(temp[win])
        temp=[deque(), deque()]
        check=[0, 0]
    t=1-t
if len(start[0])>len(start[1]):
    print('do')
elif len(start[0])<len(start[1]):
    print('su')
else:
    print('dosu')