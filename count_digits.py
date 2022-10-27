n=map(int,input().split())
l=list(input().split())
l2=[]
for i in l:
    l2.append(abs(int(i)))

for k in l2:
    k1=str(k)
    print(len(k1),end=' ')
    