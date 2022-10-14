n=int(input())
primes=[]
for i in range(n+1):
    if i>1:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            primes.append(i)

factors=[]
for u in range(1,n+1):
    if n%u==0:
        factors.append(u)
count=0
for z in factors:
    if z not in primes:
        count+=1
print(count)