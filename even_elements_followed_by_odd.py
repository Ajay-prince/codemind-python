n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
for i in l1:
    print(i,end=' ')
for j in l2:
    print(j,end=" ")