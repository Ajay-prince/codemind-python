n=input()
l=[]
for i in n:
    l.append(i)
k=set(l)
l2=list(k)
if len(l2)==len(l):
    print('Unique Number')
else:
    print('Not Unique Number')