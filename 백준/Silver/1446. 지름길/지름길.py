import sys
from collections import deque
input=sys.stdin.readline


N, D = map(int, input().split())

dist = list(range(D + 1))
Q=[]

for _ in range(N):
    start, end, length = map(int, input().split())
    if end <= D and length <  end - start:
        Q.append((start, end, length))
Q.sort(key=lambda x: x[1])

while(Q):
    start, end, length = Q.pop(0)
    dist[end] = min(dist[end], dist[start] + length)
    for i in range (end +1, D+1):
        dist[i] = min(dist[i], dist[i-1] + 1)

print(dist[D])