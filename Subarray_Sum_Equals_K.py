n,k=map(int,input().split())
l=list(map(int,input().split()))
count=0
for i in range(n):
    s=0
    for j in range(i,n):
        s+=l[j]
        if(s==k):
            count+=1
        if s>k:
            break
print(count)
