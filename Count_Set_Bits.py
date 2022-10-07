for _ in range(int(input())):
    n=int(input())
    t=0
    l=[]
    while n>0:
        re=n%2
        l.append(re)
        n=n//2
    l.reverse()
    for i in l:
        if i==1:
            t+=1
    print(t)