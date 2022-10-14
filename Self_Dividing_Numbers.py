def nums(k):
    t=k
    t1=str(k)
    l=[]
    l1=[]
    while k>0:
        re=k%10
        
        if re==0:
            break
        l.append(re)
        k=k//10
    for u in l:
        if t%u==0:
            l1.append(u)
    if (len(l1)==len(t1)):
        print(t,end=' ')

n1=int(input())
n2=int(input())
for n in range(n1,n2+1):
    if n>=10:
        nums(n)
    else:
        print(n,end=' ')

