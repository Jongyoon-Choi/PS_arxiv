import sys
input=sys.stdin.readline
INF=int(1e9)

n = int(input())
m = int(input())
dist = [[INF] * n for _ in range(n)]

for i in range(n):
    dist[i][i]=0

for _ in range(m):
    a, b, c = map(int, input().split())
    a-=1
    b-=1
    if c<dist[a][b]:
        dist[a][b]=c
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k]+dist[k][j]<dist[i][j]:
                dist[i][j]=dist[i][k]+dist[k][j]
for row in dist:
    for element in row:
        if element==INF:
            print(0, end=' ')
        else:
            print(element, end=' ')
    print()
