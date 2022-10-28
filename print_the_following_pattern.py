n=int(input())
l=[]
for j in range(1,n+1):
    l.append(j)
for k in range(n):
    for u in l:
        print(u,end='')
    print()
    l.pop()
    