t1=input()
t=t1.lower()
c=0
k=0
for i in t:
    if(i.isalpha() or i.isdigit() or i==' '):
        k+=1
    else:
        c+=1
print(c)