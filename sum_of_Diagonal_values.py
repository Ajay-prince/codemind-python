n,m=map(int,input().split())
matrix=[]
matrix2=[]
for i in range(n):
    a=list(map(int,input().split()))
    matrix.append(a)
    b=a[::-1]
    matrix2.append(b)
sum1=[]
sum2=[]
for j in range(n):
    for k in range(m):
        if j==k:
            sum1.append(matrix[j][k])
            sum2.append(matrix2[j][k])
if len(sum2)%2==0:
    sum3=sum1+sum2
    print(sum(sum3))
else:
    d=len(sum2)
    e=int(d/2)
    sum2.pop(e)
    sum3=sum1+sum2
    print(sum(sum3))