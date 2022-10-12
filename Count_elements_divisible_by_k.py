n,k=map(int,input().split())
list1=list(map(int,input().split()))
count=0
for i in list1:
    if i%k==0:
        count+=1
print(count)