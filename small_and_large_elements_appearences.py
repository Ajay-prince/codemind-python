l=input()
l2=[]
for i in l:
    l2.append(i)
for j in l2:
    if j==' ':
        l2.remove(j)
print(min(l2),l2.count(min(l2)),end=' ')
print(max(l2),l2.count(max(l2)),end=' ')
