N=int(input())
S=[]
for _ in range(N):
    S.append(input().split())
L=input().split()
psb=True
for i in range(N):
    if psb:
        pre_s=0
        for s in S[i]:
            if s in L:
                if L.index(s)>=pre_s:
                    pre_s=L.index(s)
                    L.remove(s)
            else:
                psb=False
                break
if L:
    psb=False
print('Possible' if psb else 'Impossible')