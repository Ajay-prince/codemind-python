a=int(input())
b=int(input())
n=a+b
primes=[]
for i in range(n*2):
    if i>1:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            primes.append(i)
for k in range(1,n*2):
    if (n+k) in primes:
        print(k)
        break