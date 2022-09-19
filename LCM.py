n,m=map(int,input().split())
l1=[i*n for i in range(1,110)]
l2=[i*m for i in range(1,110)]
l3=[]
for i in l1:
    for j in l2:
        if i==j:
            l3.append(int(j))
               
            break
print(min(l3))
        
