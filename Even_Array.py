n=int(input())
l=list(map(int,input().split()))
odd=[]
for i in l:
    if i%2!=0:
        odd.append(i)
if len(odd)==0:
    print('True')
else:
    print('False')