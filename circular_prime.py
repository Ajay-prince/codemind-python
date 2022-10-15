n=int(input())
t=n
if n>1:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            isprime=False
            break
    else:
        isprime=True
rev=0
while n>0:
    re=n%10
    rev=rev*10+re
    n=n//10
if rev>1:
    for j in range(2,int(rev**0.5)+1):
        if rev%j==0:
            isprime1=False
            break
    else:
        isprime1=True
if isprime==True and isprime1==True:
    print('circular prime')
elif isprime==True and isprime1==False:
    print('prime but not a circular prime')
else:
    print('not prime')
    