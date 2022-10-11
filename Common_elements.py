n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))

l3=[]
for i in l1:
    if i not in l3:
        l3.append(i)
l4=[]
for j in l3:
    if j in l2:
        l4.append(j)
for u in l4:
    print(u,end=' ')