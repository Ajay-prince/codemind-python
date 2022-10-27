s1=list(input().split())
s2=list(input().split())
str1=''
str2=''
for i in s1:
    str1+=(i.lower())
for j in s2:
    str2+=(j.lower())
l5=[]
for k in str1:
    if k not in str2:
        l5.append(k)
for a in str2:
    if a not in str1:
        l5.append(a)
l6=[]
for u in l5:
    if u not in l6:
        l6.append(u)
l7=sorted(l6)
if len(l7)!=0:
    for r in l7:
        print(r,end='')
else:
    print(-1)