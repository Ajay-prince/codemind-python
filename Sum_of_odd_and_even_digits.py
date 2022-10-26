n=int(input())
l=list(map(int,input().split()))

sume=0
sumo=0
for i in range(len(l)):
    if i%2==0:
        sume+=l[i]
    else:
        sumo+=l[i]
sumd=sume-sumo
if sumd==0:
    print('YES')
else:
    print('NO')