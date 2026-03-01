import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    n=int(input())
    candidates = []
    for _ in range(n):
        a, b = map (int, input().split())
        candidates.append((a,b))
    candidates.sort()

    min_b=200000
    count=0
    for _, b in candidates:
        if b<min_b:
            count+=1
            min_b = b 
    print(count)
