for _ in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    l1=list(map(int,input().split()))
    l2=l+l1
    l3=sorted(l2)
    print(*l3)
    