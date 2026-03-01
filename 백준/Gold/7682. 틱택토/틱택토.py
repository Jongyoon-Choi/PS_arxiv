import sys

while True:
    cmd=sys.stdin.readline().rstrip()
    if cmd=='end':
        break
    X=[]
    O=[]
    finish_case=[(0,4,8), (2,4,6), (0,1,2),(3,4,5), (6,7,8), (0,3,6), (1,4,7), (2, 5, 8)]
    for i in range(len(cmd)):
        if cmd[i]=='X':
            X.append(i)
        elif cmd[i]=='O':
            O.append(i)
    if len(X)==5 and len(O)==4:
        if any(all(c in O for c in case) for case in finish_case):
            print('invalid')
        else:
            print('valid')
    elif len(X)==len(O)+1:
        if any(all(c in X for c in case) for case in finish_case) and not any(all(c in O for c in case) for case in finish_case):
            print('valid')
        else:
            print('invalid')
    elif len(X)==len(O):
        if any(all(c in O for c in case) for case in finish_case) and not any(all(c in X for c in case) for case in finish_case):
            print('valid')
        else:
            print('invalid')
    else:
        print('invalid')