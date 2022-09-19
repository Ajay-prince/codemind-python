n=int(input())
pro=n*n
sum=0
while pro>0:
    r=pro%10
    sum+=r
    pro=pro//10
if sum==n:
    print('Neon Number')
else:
    print('Not Neon Number')
