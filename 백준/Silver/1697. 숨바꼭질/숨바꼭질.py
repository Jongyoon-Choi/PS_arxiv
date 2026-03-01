import sys
input=sys.stdin.readline


N, K = map(int, input().split())

visit = [0] * (100001)
visit[N] = 1
Q=[N]

for time in range(100001):
    new_Q = []
    for p in Q:
        if p == K:
            print(time)
            sys.exit()
        elif p > K:
            if not visit[p-1]:
                visit[p-1] = 1
                new_Q.append(p-1)
        elif p == 0:
            if not visit[p+1]:
                visit[p+1] = 1
                new_Q.append(p+1)
        else:
            if not visit[p-1]:
                visit[p-1] = 1
                new_Q.append(p-1)
            if not visit[p+1]:
                visit[p+1] = 1
                new_Q.append(p+1)
            if p*2 <= 100000 and not visit[p*2]:
                visit[p*2] = 1
                new_Q.append(p*2)
    Q = new_Q