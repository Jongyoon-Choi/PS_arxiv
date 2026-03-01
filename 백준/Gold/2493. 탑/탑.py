import sys
input=sys.stdin.readline

N = int(input())

top_list=list(map(int,input().split()))

top_list.insert(0, sys.maxsize)
temp = [0]
res= [0] * N

for i in range(1, N + 1):
    if top_list[i] > top_list[temp[-1]]:
        for idx in reversed(temp):
            if top_list[idx] < top_list[i]:
                temp.pop()
            else:
                break
    res[i-1] = temp[-1]
    temp.append(i)

print(" ".join(map(str, res)))