n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if i not in l1:
        l1.append(i)
for j in l1:
    if l.count(j)==j:
        l2.append(j)
if len(l2)!=0:
    print(min(l2),max(l2))
else:
    print(-1)
