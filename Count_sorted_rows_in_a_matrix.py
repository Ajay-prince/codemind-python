n,m=map(int,input().split())

matrix=[]
count=0
for i in range(n):
    a=list(map(int,input().split()))
    b=sorted(a)
    c=sorted(a,reverse=True)
    if a==b or a==c:
        count+=1
print(count)