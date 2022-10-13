n=input()
t=input()
n1=[]
t1=[]
for i in n:
    n1.append(i.lower())
for j in t:
    t1.append(j.lower())
n2=[]
for k in n1:
    if k not in n2:
        n2.append(k)
t2=[]
for u in t1:
    if u not in t2:
        t2.append(u)
for y in n2:
    if y==' ':
        n2.remove(y)
for g in t2:
    if g==' ':
        t2.remove(g)

count=0
for o in n2:
    if o not in  t2:
        count+=1
count1=0
for r in t2:
    if r not in n2:
        count1+=1
print(count1+count)