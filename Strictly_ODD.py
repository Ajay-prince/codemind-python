n=int(input())
l=list(map(int,input().split()))
index=[]
for i in l:
    if i%2!=0:
        index.append(l.index(i))
def odd(a):
    if a>0 and a%2==0:
        return 1
count=0
for j in index:
    if odd(j)==1:
        count+=1
if count==0:
    print(True)
else:
    print(False)