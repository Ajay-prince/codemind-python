n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
l4=[]
for i in l1:
    if i not in l2:
        l3.append(i)
for j in l2:
    if j not in l1:
        l4.append(j)
l5=l3+l4
l6=[]
for k in l5:
    if k not in l6:
        l6.append(k)
for u in l6:
    print(u,end=' ')