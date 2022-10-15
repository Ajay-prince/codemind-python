n=input()
l=[]
for i in n:
    l.append(int(i))
if len(l)==10:
    if l[0]==0:
        print('Invalid')
    else:
        print('Valid')
else:
    print('Invalid')
