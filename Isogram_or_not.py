n=input()
a=[]
for i in n:
    a.append(i)
b=[]
for j in a:
    if j not in b:
        b.append(j)
if len(b)==len(a):
    print(True)
else:
    print(False)
