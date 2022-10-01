n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i>1 or i<0:
        l1.append(int(i))
if len(l1)==0:
    print('True')
else:
    print('False')

    