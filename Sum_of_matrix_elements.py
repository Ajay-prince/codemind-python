n=int(input())
m=int(input())
matrix=[]
for i in range(n):
    a=list(map(int,input().split()))
    matrix.append(a)
sum=0
for k in range(n):
    for j in range(m):
        sum+=matrix[k][j]
print(sum)