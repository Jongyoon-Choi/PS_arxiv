import sys
input = sys.stdin.readline

N= int(input())
liquids = list(map(int, input().split()))
liquids.sort()

left, right = 0, len(liquids) - 1

if liquids[left] > 0:       # 모두 산성
    print(liquids[0], liquids[1])
elif liquids[right] < 0:    # 모두 알칼리성
    print(liquids[-2], liquids[-1])
else:   # 섞여있는 경우
    best_left = left 
    best_right = right 
    best_mixed = liquids[left] + liquids[right]
    while left != right:
        mixed = liquids[left] + liquids[right]
        if abs(mixed) < abs(best_mixed):
            best_left = left
            best_right = right
            best_mixed = mixed
        
        if mixed < 0:
            left += 1
        elif mixed > 0:
            right -= 1
        else:
            break
    print(liquids[best_left], liquids[best_right])