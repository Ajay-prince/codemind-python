n=int(input())
n1=int(input())
primes=[]

for i in range(n,n1):
    if i>1:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            primes.append(i)
for k in primes:
    print(k,end='
')
