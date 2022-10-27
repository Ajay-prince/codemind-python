n,m=map(int,input().split())

matrix=[]
for i in range(n):
    a=list(map(int,input().split()))
    matrix.append(a)

sum2=[]
for i in range(m):
    sum1=0
    for j in range(n):
        sum1+=matrix[j][i]
    sum2.append(sum1)
for k in sum2:
    print(k,end=' ')