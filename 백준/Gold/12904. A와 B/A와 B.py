import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()
for _ in range(len(T)-len(S)):
    if T[-1]=='A':
        T=T[:-1]
    else:
        T=T[-2::-1]
print(int(S==T))
