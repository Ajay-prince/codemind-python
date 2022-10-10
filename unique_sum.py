n=int(input())
list1=list(map(int,input().split()))
l1=[]
count=0
for i in list1:
    if i not in l1:
        l1.append(i)
for j in l1:
    count+=j
print(count)