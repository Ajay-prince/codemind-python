a=int(input())
sum1=0
for i in range(1,a):
    if a%i==0:
        sum1+=i

b=int(input())
sum2=0
for i in range(1,b):
    if b%i==0:
        sum2+=i
if (sum2==a) and (sum1==b):
    print("Amicable")
else:
    print("Not Amicable")