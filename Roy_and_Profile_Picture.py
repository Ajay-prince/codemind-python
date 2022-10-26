n=int(input())

t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    
    if a<n or b<n:
        print('UPLOAD ANOTHER')
    elif a>=n and b>=n and a==b:
        print('ACCEPTED')
    elif a>n and b>n:
        print('CROP IT')
    else:
        print('CROP IT')