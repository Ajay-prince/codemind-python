n=int(input())
li1=list(map(int,input().split()))
c=0
for i in li1:
    t=i
    rev=0
    while t>0:
        rev=rev*10+t%10
        t=t//10
    if rev==i:
        c+=1
print(c)