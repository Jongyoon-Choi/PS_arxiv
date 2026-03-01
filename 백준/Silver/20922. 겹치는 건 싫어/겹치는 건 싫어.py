import sys
from collections import deque
input=sys.stdin.readline

n, k = map(int,input().split())

nums=list(map(int, input().split()))

left, right=0, 0
nums_count={}
max_len = 0

while right < n:
    num=nums[right]
    
    if num not in nums_count:
        nums_count[num]=1
    else:
        nums_count[num]+=1
    
    while nums_count[num] > k:
        left_num=nums[left]
        nums_count[left_num]-=1
        if nums_count[left_num]==0:
            del nums_count[left_num]
        left+=1
    
    max_len = max(max_len, right - left + 1)
    
    right+=1
print(max_len)