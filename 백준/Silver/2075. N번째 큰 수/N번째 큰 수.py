import sys
input=sys.stdin.readline
n = int(input())
nums=list(map(int,input().split()))
for i in range(1, n):
    nums.extend(list(map(int,input().split())))
    nums.sort(reverse=True)
    nums=nums[:n]

print(nums[-1])