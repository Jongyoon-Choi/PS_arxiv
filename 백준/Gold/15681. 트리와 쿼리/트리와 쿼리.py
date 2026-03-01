import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

N, R, Q=map(int, input().split())
tree=[[]for _ in range(N+1)]
count=[0]*(N+1)
def countCulc(x):
    count[x]=1
    for t in tree[x]:
        if count[t]==0:
            countCulc(t)
            count[x]+=count[t]

for i in range(N-1):
    a, b=(map(int, input().split()))
    tree[a].append(b)
    tree[b].append(a)

countCulc(R)
for _ in range(Q):
    print(count[int(input())])