import sys

str1=list(sys.stdin.readline().rstrip())
str2=[]
for _ in range(int(sys.stdin.readline())):
    cmd=sys.stdin.readline().split()
    if cmd[0]=='L' and str1:
        str2.append(str1.pop())
    elif cmd[0]=='D' and str2:
        str1.append(str2.pop())
    elif cmd[0]=='B' and str1:
        str1.pop()
    elif cmd[0]=='P':
        str1.append(cmd[1])
str2.reverse()
str1.extend(str2)
print(''.join(str1))