str=input()
count=0
res=0
for i in range(len(str)):
    if str[i]=='(':
        count+=1
    elif str[i-1]=='(':
        count-=1
        res+=count
    else:
        count-=1
        res+=1
print(res)
        
        