import sys
input = sys.stdin.readline

N, M = map(int, input().split())
costs=[]
for _ in range(N):
    costs.append(int(input()))
left=max(costs)
right=sum(costs)
while left < right:
    mid = (left + right) // 2
    count = 1
    balance = mid
    for cost in costs:
        if balance - cost < 0:
            balance = mid
            count += 1
        balance -= cost
    if count > M:
        left = mid + 1
    else:
        right = mid -1
print(left)