a,b=map(int,input().split())

if a==0 and b%2==1:
    print('NO')
elif b==0 and a%2==1:
    print('NO')
elif (a*1+b*2)%2==0:
    print('YES')
else:
    print('NO')