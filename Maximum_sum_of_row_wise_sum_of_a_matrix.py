n,m=map(int,input().split())

matrix=[]
for i in range(n):
    a=list(map(int,input().split()))
    matrix.append(a)

sum2=[]
for i in range(n):
    sum1=0
    for j in range(m):
        sum1+=matrix[i][j]
    sum2.append(sum1)
print(max(sum2))