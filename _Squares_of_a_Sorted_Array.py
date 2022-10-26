n=int(input())
l=list(map(int,input().split()))
l2=[]
for i in l:
    l2.append(abs(i))
l3=sorted(l2)
for k in l3:
    print(k*k,end=' ')