n=int(input())
t=n
pro=1
sum=0
while n>0:
    r=n%10
    for i in range(1,r+1):
        pro*=i
    
    sum+=pro
    pro-=pro
    pro=1
    n=n//10
if t==sum:
    print('The number',t,'is a strong number')
else:
    print('The number',t,'is not a strong number')
