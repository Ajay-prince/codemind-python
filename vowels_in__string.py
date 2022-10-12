n=input()
vowel=['a','e','i','o','u','A','E','I','O','U']
l=[]
for i in n:
    if i in vowel:
        l.append((i))
l1=[]
for k in l:
    if k not in l1:
        l1.append(k)
if len(l1)!=0:
    for j in l1:
        print(j,end=' ')
else:
    print(-1)