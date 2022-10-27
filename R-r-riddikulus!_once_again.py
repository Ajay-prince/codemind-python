n,m=map(int,input().split())
l=list(map(int,input().split()))
l2=l[m:]+l[:m]
for i in l2:
    print(i,end=' ')
