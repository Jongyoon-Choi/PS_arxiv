from collections import deque
n,m=map(int,input().split())
dq=deque([*range(1, n+1)])
cmd=list(map(int,input().split()))
count=0
for i in range(m):
    target_idx=dq.index(cmd[i])
    if target_idx<len(dq)/2:
        for _ in range(target_idx):
            dq.rotate(-1)
            count+=1
    else:
        for _ in range(len(dq)-target_idx):
            dq.rotate(1)
            count+=1
    dq.popleft()
print(count)