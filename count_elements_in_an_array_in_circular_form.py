n=int(input())
l=list(map(int,input().split()))
c=0
l.insert(n,l[0])
l.insert(n+1,l[1])
for i in range(1,len(l)-1):
    if(l[i-1]%2==0 and l[i+1]%2) or (l[i+1]%2==0 and l[i-1]%2):
        c+=1
print(c)