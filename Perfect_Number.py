n=int(input())
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
sum=0
for j in l:
    sum+=j
if sum==n:
    print('True')
else:
    print('False')