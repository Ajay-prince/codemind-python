n=int(input())
index_o=[]
l=list(map(int,input().split()))
for i in range(len(l)):
    if l[i]%2!=0:
        index_o.append(l[i])

index_o.reverse()
for i in index_o:
    print(i)
    break