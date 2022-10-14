n=int(input())

t=n
l=[]
primes=[]
prime1=[]
for i in range(n*2):
    if i>1:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            primes.append(i)

while n>0:
    re=n%10
    prime1.append(re)
    n=n//10
for k in prime1:
    if k not in primes:
        l.append(False)
if len(l)==0 and t in primes:
    print('Mega Prime')
else:
    print('Not Mega Prime')
        