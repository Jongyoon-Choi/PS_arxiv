N=int(input())
snack=[]
apple=[]
turn=[]
K=int(input())
for _ in range(K):
    r,c=map(int,input().split())
    apple.append((r,c))
L=int(input())
for _ in range(L):
    t,d=input().split()
    turn.append((int(t), d))
time=0
r, c=1,1
direction=0
while r>0 and r<=N and c>0 and c<=N:
    time+=1
    snack.append((r,c))
    if direction==0:
        c+=1
    elif direction==1:
        r+=1
    elif direction==2:
        c-=1
    else:
        r-=1
    if (r,c) in snack:
        break
    if (r,c) not in apple:
        snack.pop(0)
    else:
        apple.remove((r, c))
    if turn and time==turn[0][0]:
        d=turn.pop(0)[1]
        direction=(direction+ (1 if d=='D' else 3))%4
print(time)