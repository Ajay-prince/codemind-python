r=int(input())
matrix1=[]
matrix2=[]
for j in range(r):
    a=list(map(int,input().split()))
    matrix1.append(a)
for k in range(r):
    b=list(map(int,input().split()))
    matrix2.append(b)
matrix=[]
for k in range(r):
    c=[]
    for u in range(r):
        c.append(abs(matrix1[k][u]-matrix2[k][u]))
    matrix.append(c)
for y in matrix:
    print(*y)