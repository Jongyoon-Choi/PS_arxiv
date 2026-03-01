import sys
input=sys.stdin.readline
n = int(input())
nums=list(map(int,input().split()))
res=[]
for i in range(n):
    res.insert(nums.pop(), n)
    n-=1
print(' '.join(map(str, res)))