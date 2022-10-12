a=int(input())
li1=list(map(int,input().split()))
l=[]
for i in li1:
    t=i
    sum1=0
    while t>0:
        re=t%10
        sum1+=1
        t=t//10
    l.append(sum1)
c=0
d=min(l)
for j in l:
    if j==d:
        c+=1
print(c)