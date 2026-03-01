N=int(input())
S=[]
for _ in range(N):
    S.append(list(map(int, input().split())))
S=sorted(S,key=lambda x: x[0])
max_s=S.index(max(S,key=lambda x: x[1]))
space=0
w=S[0][0]
h=S[0][1]
for i in range(1,max_s+1):
    if S[i][1]>=h:
        space+=h*(S[i][0]-w)
        w=S[i][0]
        h=S[i][1]
w=S[-1][0]
h=S[-1][1]
for i in range(len(S)-1,max_s-1,-1):
    if S[i][1]>=h:
        space+=h*(w-S[i][0])
        h=S[i][1]
        w=S[i][0]
space+=S[max_s][1]
print(space)