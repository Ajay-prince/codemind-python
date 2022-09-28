n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
l1=[]
l2=[]
for i in range(a,b+1):
    l1.append(i)
for j in l:
    if j not in l1:
        l2.append(j)
   
if len(l2)!=0:
    for i in l2:
        print(i,end=" ")
else:
    print(-1)
