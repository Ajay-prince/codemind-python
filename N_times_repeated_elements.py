n=int(input())
l=list(map(int,input().split()))
n1=int(input())
l1=[]
l2=[]
for i in l:
    if i not in l1:
        l1.append(i)
for j in l1:
    if l.count(j)==n1:
        l2.append(j)
if len(l2)!=0:
    for k in l2:
        print(k,end=' ')
else:
    print(-1)