n,m=map(int,input().split())
n1=str(n)
m1=str(m)
n2=int(n1[:m])

rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
m2=str(rev)
m3=int(m2[:m])
rev1=0
while m3>0:
    r=m3%10
    rev1=rev1*10+r
    m3=m3//10
print(abs(n2-rev1))