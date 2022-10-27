n=int(input())
l=list(input().split())
l2=[]
for i in l:
    l2.append(len(i))
d=max(l2)
for k in l:
    if len(k)==d:
        print(k,end=' ')
