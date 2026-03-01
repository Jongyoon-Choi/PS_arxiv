import sys
input=sys.stdin.readline

points=[]
N=int(input())
for _ in range(N):
    points.append(list(map(int, input().split())))
a=0
b=0
for i in (range(N-1)):
    a+=points[i][0]*points[i+1][1]
    b+=points[i+1][0]*points[i][1]
a+=points[-1][0]*points[0][1]
b+=points[0][0]*points[-1][1]
res=abs(a-b)/2
print(res)