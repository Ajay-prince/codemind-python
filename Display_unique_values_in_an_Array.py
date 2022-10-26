n=int(input())
l=list(map(int,input().split()))
l2=[]
for i in l:
    if l.count(i)==1:
        l2.append(i)
if len(l2)!=0:
    for k in l2:
        print(k,end=' ')
else:
    print(-1)