n=int(input())
l=list(map(int,input().split()))
pro=1
l2=[]
for i in l:
    pro*=i
for j in l:
    p1=int(pro/j)
    l2.append(p1)
for k in l2:
    print(k,end=' ')