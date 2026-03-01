import sys
n,p=map(int,sys.stdin.readline().split())
count=0
gtr=[[] for _ in range(n)]
for _ in range(n):
    i,j=map(int,sys.stdin.readline().split())
    if not gtr[i-1] or gtr[i-1][-1]<j:
        gtr[i-1].append(j)
    elif gtr[i-1][-1]==j:
        continue
    else:
        while gtr[i-1] and gtr[i-1][-1]>j:# 큰거 다 빼기
            gtr[i-1].pop()
            count+=1
        if not gtr[i-1] or gtr[i-1][-1]<j:
            gtr[i-1].append(j)
        else:
            continue
    count+=1
print(count)