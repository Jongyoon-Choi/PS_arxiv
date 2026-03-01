import sys
input=sys.stdin.readline

n, m = map(int,input().split())

graph = []
res = [[-1]*m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    ipt=list(map(int,input().split()))
    graph.append(ipt)
    
    if 2 in ipt:
        target_i=i
        target_j=ipt.index(2)
        
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            res[i][j]=0
            
queue=[(target_i, target_j, 0)]

while queue:
    i, j, dist = queue.pop(0)
    if graph[i][j]==0 or visited[i][j]:
        continue
    
    visited[i][j]=True
    
    res[i][j]=dist
    near=[(i-1, j), 
          (i, j-1),
          (i+1, j), 
          (i, j+1)]
        
    for p, q in near:
        if 0 <= p <n and 0 <= q < m and not visited[p][q]:
            queue.append((p, q, dist+1))
            
for row in res:
    print(' '.join(map(str, row)))