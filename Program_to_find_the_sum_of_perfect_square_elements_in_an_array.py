n=int(input())
l=list(map(int,input().split()))
l2=[]
for i in l:
    t=int((i**0.5))
    if (i==(t*t)):
        l2.append(i)
if len(l2)!=0:
    print(sum(l2))
else:
    print(-1)