n,m=map(int,input().split())
l=list(input().split())
count=0
l2=[]
for i in l:
    l2.append(abs(int(i)))
for k in l2:
    k1=str(k)
    if len(k1)==m:
        count+=1
print(count)