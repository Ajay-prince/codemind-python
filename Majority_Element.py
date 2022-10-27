n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
        
l2=[]
for j in l1:
    l2.append(l.count(j))
d=max(l2)
for k in l1:
    if l.count(k)==d:
        print(k)