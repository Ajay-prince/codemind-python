a,b=map(int,input().split())
if b==a+1 or a+b==11:
    print('Yes')
elif b==a-1:
    print('Yes')
else:
    print('No')