n=int(input())
list1=list(map(int,input().split()))

l1=[]
for i in range(len(list1)-1):
    if list1[i]<list1[i+1]:
        l1.append(True)
    else:
        l1.append(False)
        
l2=sorted(l1)

for i in l2:
    if i==True:
        print('yes')
        break
    else:
        print('no')
        break