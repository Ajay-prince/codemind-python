t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    d=[]
    if(n%2==0):
        for i in range(0,len(l)//2):
            d.append(l[n-i-1])
            d.append(l[i])
    else:
        for i in range(0,len(l)//2):
            d.append(l[n-i-1])
            d.append(l[i])
        d.append(l[n//2])
    print(*d)