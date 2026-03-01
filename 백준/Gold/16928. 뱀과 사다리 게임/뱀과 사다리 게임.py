import sys
from collections import deque
input=sys.stdin.readline


N, M = map(int, input().split())

ladder = dict()
snake = dict()

for i in range(N):
    x, y = map(int, input().split())
    ladder[x]= y

for i in range(M):
    u, v = map(int, input().split())
    snake[u]=v

visit = [0] * 101

Q = deque()
Q.append(1)

cnt=0
flag = True

while flag:
    length = len(Q)
    
    for _ in range(length):
        x = Q.popleft()

        if x == 100:
            print(cnt)
            flag =False
            break

        for i in range(1, 7):
            new_x = x + i

            if new_x <= 100 and visit[new_x] == 0:
                visit[new_x]= 1

                if new_x in ladder.keys():
                    visit[ladder[new_x]]=1
                    Q.append(ladder[new_x])

                elif new_x in snake.keys():
                    visit[snake[new_x]]=1
                    Q.append(snake[new_x])

                else:
                    Q.append(new_x)
    cnt += 1


