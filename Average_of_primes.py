n=int(input())
list1=list(map(int,input().split()))
l2=[]
for i in list1:
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            l2.append(i)
avg=sum(l2)/len(l2)
avg1="{:.2f}".format(avg)
print(avg1)
