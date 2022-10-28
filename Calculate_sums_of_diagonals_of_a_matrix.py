n=int(input())
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
    for k in range(n):
        if j==k:
            sum1.append(matrix[j][k])
            sum2.append(matrix2[j][k])
p='Principal Diagonal:'
s='Secondary Diagonal:'
p+=str(sum(sum1))
s+=str(sum(sum2))
print(p)
print(s)