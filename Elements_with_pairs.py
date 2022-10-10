n=int(input())
list1=list(map(int,input().split()))
list2=[]
for i in list1:
    list2.append(i)
if len(list2)%2!=0:
    list2.append(0)
for k in list2:
    print(k,end=' ')