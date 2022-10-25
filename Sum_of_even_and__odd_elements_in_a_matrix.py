r,c=map(int,input().split())
matrix=[]
for i in range(r):
    a=list(map(int,input().split()))
    matrix.append(a)
sum1=0
sum2=0
for k in range(r):
    for u in range(c):
        if (matrix[k][u]%2==0):
            sum1+=matrix[k][u]
        else:
            sum2+=matrix[k][u]
print(sum1,sum2)