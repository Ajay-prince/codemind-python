n=int(input())
l=map(int,input().split())
unique=[]
for i in l:
    if i not in unique:
        unique.append(i)
for j in unique:
    print(j,end=' ')