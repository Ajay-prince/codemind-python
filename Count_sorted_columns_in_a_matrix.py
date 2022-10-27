n,m=map(int,input().split())

matrix=[]
count=0
for i in range(n):
    a=list(map(int,input().split()))
    matrix.append(a)
for j in range(m):
    l=[]
    for k in range(n):
        l.append(matrix[k][j])
    b=sorted(l)
    c=sorted(l,reverse=True)
    if l==b or l==c:
        count+=1
print(count)