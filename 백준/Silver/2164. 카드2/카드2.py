from collections import deque
n=int(input())
dq=deque([*range(n)])
while len(dq)!=1:
    dq.popleft()
    dq.rotate(-1)
print(dq.popleft()+1)