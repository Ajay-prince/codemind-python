n=int(input())
pro=1
sum=0
while n>0:
    r=n%10
    pro*=r
    sum+=r
    n=n//10
if pro==sum:
    print('Spy Number')
else:
    print('Not Spy Number')