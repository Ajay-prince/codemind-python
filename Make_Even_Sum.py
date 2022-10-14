n=int(input())
sum=0
list1=list(map(int,input().split()))
for i in list1:
    sum+=i
if sum%2==0:
    print(1)
else:
    print(0)