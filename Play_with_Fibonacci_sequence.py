n=int(input())
a=0
b=1
l=[]
l.append(a)
l.append(b)
for i in range(n*n):
    c=a+b
    l.append(c)
    a=b
    b=c
k=0
for j in l:
    print(j,end=' ')
    k+=1
    if k==n:
        break
    