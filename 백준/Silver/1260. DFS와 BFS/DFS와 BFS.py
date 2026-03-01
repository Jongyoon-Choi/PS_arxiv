import sys
input=sys.stdin.readline

N, M, V=map(int,input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    a, b = map(int,input().split())
    graph[a][b] = graph[b][a] = True
    
visited1 = [False] * (N + 1)  # dfs의 방문기록
visited2 = visited1.copy()

def dfs(V):
    visited1[V]=True
    print(V,end=' ')
    for i in range(1, N+1):
        if graph[V][i] and not visited1[i]:
            dfs(i)

def bfs(V):
    q=[V]
    visited2[V]=True
    while q:
        V=q.pop(0)
        print(V, end=' ')
        for i in range(1,N+1):
            if graph[V][i] and not visited2[i]:
                q.append(i)
                visited2[i]=True
    
        
        
dfs(V)
print()
bfs(V)