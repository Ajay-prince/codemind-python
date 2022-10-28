n=int(input())
matrix=[]
for i in range(n):
    l=[]
    for j in range(1,n+1):
        l.append(j)
    matrix.append(l)
    n-=1
matrix.reverse()
for y in matrix:
    for k in y:
        print(k,end='')
    print()