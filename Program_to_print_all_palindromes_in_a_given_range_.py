n=int(input())
n1=int(input())
for i in range(n,n1):
    t=i
    rev=0
    while i>0:
        re=i%10
        rev=rev*10+re
        i=i//10
    if t==rev:
        print(t,end=' ')