from collections import deque
n,k,m=map(int,input().split())
dq=deque([*range(n)])
res = []
while dq:
    if int((n-len(dq))/m)%2==0:
        dq.rotate(-k+1)
    else:
        dq.rotate(k)
    res.append(str(dq.popleft()+1))
for num in res:
    print(num)