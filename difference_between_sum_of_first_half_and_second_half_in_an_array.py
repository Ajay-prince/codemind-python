n=int(input())
list1=list(map(int,input().split()))
sum1=0
sum2=0
l1=len(list1)//2
for i in range(l1):
    sum1+=list1[i]
for j in range(l1,len(list1)):
    sum2+=list1[j]
print(abs(sum1-sum2))