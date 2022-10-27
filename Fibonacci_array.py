n=int(input())
l=list(map(int,input().split()))

a=l[0]
b=l[1]
l1=[]
l1.append(a)
l1.append(b)
for i in range(len(l)-2):
    c=a+b
    l1.append(c)
    a=b
    b=c
l2=[]
for j in range(len(l)):
    if l[j]!=l1[j]:
        l2.append(False)
        
if len(l2)==0 and n>2:
    print('yes')
else:
    print('no')