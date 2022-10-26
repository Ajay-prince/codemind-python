n=int(input())
l=list(map(int,input().split()))
l2=[]
for i in l:
    count=0
    
    for j in l:
        if i>j:
            count+=1
    l2.append(count)
for k in l2:
    print(k,end=' ')
        