n=int(input())
birth_list={}
for i in range(n):
    name_birth=list(input().split())
    name_birth[1:]=map(int,name_birth[1:])
    birth_list[name_birth[0]]=name_birth[3]*10000+name_birth[2]*100+name_birth[1]
birth_list=sorted(birth_list.items(), key=lambda item: item[1])
print(birth_list[n-1][0]+ '\n'+ birth_list[0][0])