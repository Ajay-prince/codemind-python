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

print(len(l2))