import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heights=list(map(int, input().split()))
left=0
right=max(heights)
while left <= right:
    mid = (left + right) // 2
    total = 0
    for height in heights:
        if height > mid:
            total += height - mid
            if total >= M:
                break
    if total >= M:
        left = mid + 1
    else:
        right = mid -1
print(right)