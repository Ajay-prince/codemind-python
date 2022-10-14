a=int(input())
primes=[]
for i in range(1,a*2):
    if i>1:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            primes.append(i)
prime1=[]   
for k in primes:
    if a%k==0:
        prime1.append(k)
if len(prime1)!=0 and len(prime1)!=1:
    
    for u in prime1:
        print(u,end=' ')
else:
    print(-1)