n=int(input())
list1=list(map(int,input().split()))
li=[]
for i in list1:
    if list1.count(i)==1:
        li.append(i)
for j in li:
    print(j,end=' ')