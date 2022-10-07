n=int(input())
t=str(n)
k=''
sum=0
l1=[]
l=[]
while n>0:
    rem=n%2
    l.append(rem)
    n=n//2
i=0
l.reverse()
for i in l:
    if i==0:
        l1.append(1)
    else:
        l1.append(0)

for j in l1:
    k+=str(j)
k1=int(k)
f=0
while f<len(k):
    re=k1%10
    sum+=re*pow(2,f)
    k1=k1//10
    f+=1
print(sum)


