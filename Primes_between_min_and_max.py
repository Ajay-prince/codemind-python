n=int(input())
prime=[]
l=list(map(int,input().split()))

n=l.index(min(l))
m=l.index(max(l))
if n>m:
    n,m=m,n
for i in range(n,m+1):
    prime.append(l[i])

count=0
for k in prime:
    if k>1:
        for j in range(2,int(k**0.5)+1):
            if k%j==0:
                break
        else:
            count+=1
print(count)