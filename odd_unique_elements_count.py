n=int(input())
li=list(map(int,input().split()))
l1=[]
count=0
for i in li:
    if i not in l1:
        l1.append(i)
for j in l1:
    if j%2!=0:
        count+=1
print(count)