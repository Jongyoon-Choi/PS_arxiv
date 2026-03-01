import sys
input=sys.stdin.readline

N = int(input())

balls = list(input()[:-1])

count_R=0
count_B=0

min_R=500000
min_B=500000

for ball in balls:
    if ball=='R':
        count_R+=1
    else:
        count_B+=1

min_R=count_R
min_B=count_B

n=0
for ball in balls:
    if ball==balls[0]:
        n+=1
    else:
        if balls[0]=='R':
            min_R=min(min_R, count_R-n)
        else:
            min_B=min(min_B, count_B-n)
        break
n=0
for ball in balls[::-1]:
    if ball==balls[-1]:
        n+=1
    else:
        if balls[-1]=='R':
            min_R=min(min_R, count_R-n)
        else:
            min_B=min(min_B, count_B-n)
        break
print(min(min_R, min_B))