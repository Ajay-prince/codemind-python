r,c=map(int,input().split())
matrix=[]
for i in range(r):
    a=list(map(int,input().split()))
    matrix.append(a)
for k in range(r):
    sum2=0
    for u in range(c):
        sum2+=matrix[k][u]
    print(sum2,end=' ')