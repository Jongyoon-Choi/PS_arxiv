n=int(input())
for i in range(n):
    count=0
    N, M=map(int,input().split())
    importance=list(map(int,input().split()))
    while importance:
        if importance[0]<max(importance):
            importance.append(importance.pop(0))
            M=(M+len(importance)-1)%len(importance)
        elif M==0:
            count+=1
            print(count)
            break
        else:
            count+=1
            M-=1
            importance.pop(0)