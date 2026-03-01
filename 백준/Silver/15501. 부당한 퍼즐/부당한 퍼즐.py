from collections import deque
import sys
n=int(sys.stdin.readline())
cmd=deque(sys.stdin.readline().split())
res=deque(sys.stdin.readline().split())
rev_res=deque(reversed(res))
good=False
for _ in  range(n):
    if cmd==res or cmd==rev_res:
        good=True
        break
    cmd.rotate(1)
print('good puzzle' if good else 'bad puzzle')