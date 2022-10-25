r,c=map(int,input().split())
matrix=[]
for i in range(r):
    a=list(map(int,input().split()))
    matrix.append(a)
sum1=0
sum2=0
for k in range(r):
    for u in range(c):
        sum2+=matrix[k][u]
for i in range(r):
    for j in range(c):
        if i==0:
            sum1+=matrix[i][j]
        if (i%2==0) and i>0:
            sum1+=matrix[i][j]
print(sum1,abs(sum2-sum1))
       
