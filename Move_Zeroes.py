n=int(input())
l=list(map(int,input().split()))
l2=[]
count=0
for i in l:
    if i!=0:
        l2.append(i)
    else:
        count+=1
for j in range(count):
    l2.append(0)
for k in l2:
    print(k,end=' ')