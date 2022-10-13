n=list(input().split())
t=list(input().split())
n1=[]
for i in n:
    n1.append(i.lower())
t1=[]
for j in t:
    t1.append(j.lower())
count=0
for w in n1:
    for u in t1:
        if w==u:
            count+=1
print(count)

