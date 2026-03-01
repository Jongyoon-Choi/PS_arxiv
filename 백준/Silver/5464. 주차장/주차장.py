import sys
n, m=map(int,sys.stdin.readline().split())
fee=[]
weight=[]
use = [0] * n
wait=[]
total=0
for _ in range(n):
    fee.append(int(sys.stdin.readline()))
for _ in range(m):
    weight.append(int(sys.stdin.readline()))
for _ in range(2*m):
    cmd=int(sys.stdin.readline())
    if cmd>0:
        if 0 in use:
            for i in range(n):
                if use[i]==0:
                    use[i]=cmd
                    break
        else:
            wait.append(cmd)
    else:
        idx=use.index(-cmd)
        use[idx]=0
        total+=weight[-cmd-1]*fee[idx]
        if wait:
            use[idx]=wait.pop(0)
print(total)