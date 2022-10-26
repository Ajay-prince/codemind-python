n=int(input())
l1=list(map(int,input().split()))
l2=l1
b=int(n/2)
l1.reverse()
l3=l2[b:]
l3.reverse()
l4=l1[:b]+l3
for i in l4:
    print(i,end=' ')