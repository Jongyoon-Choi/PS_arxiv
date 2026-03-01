import sys
sys.setrecursionlimit(10**6)

n, m=map(int, sys.stdin.readline().split())
parent=[0]*(n+1)
for i in range(n+1):
    parent[i]=i
def find(a):#루트 노드 찾기
    if parent[a]==a:
        return a
    p = find(parent[a]) # a의 루트 노드 찾기
    parent[a] = p # 부모 테이블 갱신
    return parent[a] # a의 루트 노드 반환

def union(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return
    elif a<b:
        parent[b]=a
    else:
        parent[a]=b

for i in range(m):
    cmd=list(map(int, sys.stdin.readline().split()))
    if cmd[0]==0:
        union(cmd[1],cmd[2])
    else:
        if find(cmd[1])==find(cmd[2]):
            print('yes')
        else:
            print('no')