a=int(input())
li1=list(map(int,input().split()))
sum=0
for i in li1:
    t=i
    sum1=0
    while t>0:
        re=t%10
        sum1+=re
        t=t//10
    sum+=sum1
print(sum)