n=int(input())
t=n
sum=0
i=0
while n>0:
    rem=n%10
    sum+=rem*pow(8,i)
    n=n//10
    i+=1

l=[]
while sum>0:
    re=sum%2
    l.append(re)
    sum=sum//2

l.reverse()
for i in l:
    print(i,end="")

