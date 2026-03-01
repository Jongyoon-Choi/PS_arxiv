import sys
input = sys.stdin.readline

N = int(input())
nums = [0]
for _ in range(N):
    nums.append(int(input()))

result = set()
for i in range(1, N+1):
    temp = i
    for _ in range(N):
        temp = nums[temp]
        if temp == i:
            result.add(i)
            break

print(len(result))
for n in sorted(result):
    print(n)