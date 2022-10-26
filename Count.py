n=int(input())
l=list(map(int,input().split()))
sume=0
sumo=0
for i in l:
    if i%2==0:
        sume+=1
    else:
        sumo+=1
print(sume,sumo)
