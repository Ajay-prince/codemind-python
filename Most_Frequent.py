n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
count=[]
for j in l1:
    count.append(l.count(j))
d=max(count)
l2=[]
for k in l1:
    if l.count(k)==d:
        l2.append(k)
print(min(l2))