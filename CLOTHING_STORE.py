n=int(input())
l=list(map(int,input().split()))
l2=[]
l3=[]
for i in l:
    if i not in l2:
        l2.append(i)
for j in l2:
    l3.append(l.count(j))
sum=0
for k in l3:
    sum+=int(k/2)
print(sum)