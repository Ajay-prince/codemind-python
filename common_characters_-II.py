n=input()
t=input()
n1=[]
for i in n:
    n1.append(i.lower())
t1=[]
for j in t:
    t1.append(j.lower())
n3=[]
for k in n1:
    for  z in t1:
        if k==z:
            n3.append(k)
n2=[]
for k in n3:
    if k not in n2:
        n2.append(k)
for u in n2:
    if u==' ':
        n2.remove(u)
print(len(n2))
