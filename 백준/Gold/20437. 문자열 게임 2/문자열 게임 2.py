# 20437 문자열 게임 2
import sys
input=sys.stdin.readline


T = int(input())

for _ in range(T):
    Q = []
    visited = [0] * 26

    W = input().strip()
    K = int(input())
    for i in range(len(W)):
        if not visited[ord(W[i]) - 97]: # 알파벳 방문 여부
            visited[ord(W[i]) - 97] = 1
            point = [i]
            for j in range(i+1, len(W)):
                if W[i] == W[j]:
                    point.append(j)
            # point에서 K 값에 맞게 Q에 추가
            for k in range(len(point) - K + 1):
                Q.append(point[k+K-1] - point[k] + 1)
    if Q:
        Q.sort()
        print(Q[0], Q[-1])
    else:
        print(-1)