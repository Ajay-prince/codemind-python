n=int(input())
l=list(map(int,input().split()))
t=int(input())
if t in l:
    ind=l.index(t)
    print(ind)
else:
    print(-1)