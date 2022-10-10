n=int(input())
list1=list(map(int,input().split()))
list2=[]
for x in list1:
    if x not in list2:
        list2.append(x)
sum=0
for i in list2:
    if i%2==0:
        sum+=i
print(sum)