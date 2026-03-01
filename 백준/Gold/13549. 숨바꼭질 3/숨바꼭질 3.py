import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

dist = [-1] * (100001)
Q = deque()

flag = True
Q.append(n)
dist[n]=0

while flag:
    x = Q.popleft()
    
    if x == k:
        print(dist[x])
        flag = False

    if 2 * x <= 100000 and dist[2 * x] == -1:
        dist[2 * x] = dist[x]
        Q.appendleft(2 * x)
    if x - 1 >= 0 and dist[x - 1] == -1:
        dist[x - 1] = dist[x] + 1
        Q.append(x - 1)
    if x + 1 <= 100000 and dist[x + 1] == -1:
        dist[x + 1] = dist[x] + 1
        Q.append(x + 1)