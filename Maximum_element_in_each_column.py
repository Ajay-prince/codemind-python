n,m=map(int,input().split())
matrix=[]
for i in range(n):
    a=list(map(int,input().split()))
    matrix.append(a)
for j in range(m):
    l=[]
    for k in range(n):
        l.append(matrix[k][j])
    print(max(l))