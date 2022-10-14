for _ in range(int(input())):
    a=int(input())
    primes=[]
    for i in range(1,a*2):
        if i>1:
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    break
            else:
                primes.append(i)
    for o in primes:
        if o>=a:
            p1=o
            
            break
    primes.reverse()
    for k in primes:
        if k<a:
            p2=k
            
            break
    p3=abs(a-p1)
    p4=abs(a-p2)
    if p3<p4:
        print(p1)
    else:
        print(p2)
        